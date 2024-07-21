const Todo = require('../models/Todo');

exports.createTodo = async (req, res) => {
    try {
        const { title, description } = req.body;
        const todo = new Todo({
            userId: req.user.id,
            title,
            description
        });
        await todo.save();
        res.status(201).json(todo);
    } catch (error) {
        res.status(400).send(error.message);
    }
};

exports.getTodos = async (req, res) => {
    try {
        const todos = await Todo.find({ userId: req.user.id });
        res.status(200).json(todos);
    } catch (error) {
        res.status(400).send(error.message);
    }
};

exports.updateTodo = async (req, res) => {
    try {
        const { id } = req.params;
        const { title, description, completed } = req.body;
        const todo = await Todo.findByIdAndUpdate(id, { title, description, completed }, { new: true });
        res.status(200).json(todo);
    } catch (error) {
        res.status(400).send(error.message);
    }
};

exports.deleteTodo = async (req, res) => {
    try {
        const { id } = req.params;
        await Todo.findByIdAndDelete(id);
        res.status(200).send('Todo deleted');
    } catch (error) {
        res.status(400).send(error.message);
    }
};
