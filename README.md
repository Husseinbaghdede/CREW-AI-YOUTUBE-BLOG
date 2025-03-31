# CrewAI YouTube Blog Generator

An intelligent blog post generator that extracts insights from YouTube videos and transforms them into comprehensive, well-structured blog articles.

## Overview

This project leverages CrewAI to orchestrate a team of AI agents that work together to research YouTube content and generate professional blog posts. The system specifically focuses on extracting information from specified YouTube channels (used channel for default: @krishnaik06) on technical topics like AI, Machine Learning, Deep Learning, and Data Science.

## Features

- **YouTube Content Research**: Automatically extracts content and insights from specified YouTube channels
- **Intelligent Content Generation**: Transforms video content into coherent, well-structured blog articles
- **Agent Collaboration**: Uses multiple specialized AI agents that collaborate on different aspects of the workflow
- **Sequential Process**: Implements a structured workflow for research and content creation
- **Persistent Memory**: Maintains context throughout the task execution process

## Architecture

The project follows a modular architecture with the following components:

### Agents

- **Blog Researcher**: Specializes in extracting relevant information from YouTube videos
- **Blog Writer**: Transforms research into compelling narrative content

### Tasks

- **Research Task**: Identifies and analyzes relevant YouTube videos
- **Write Task**: Creates comprehensive blog content based on research findings

### Tools

- **YouTube Channel Search Tool**: Facilitates extraction of content from specific YouTube channels

## Setup and Installation

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```
   OPENAI_API_KEY=your-openai-api-key
   ```

## Usage

```python
from crew import crew

# Execute the workflow with your desired topic
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL VS Data Science'})
print(result)
```

The output will be saved in `new-blog-post.md`.

## Project Structure

```
├── agents.py          # Defines AI agents with specific roles and capabilities
├── crew.py            # Sets up the CrewAI workflow and execution
├── tasks.py           # Defines tasks to be executed by agents
├── tools.py           # Contains tools used by agents
├── requirements.txt   # Project dependencies
└── new-blog-post.md   # Output file for generated blog content
```

## Dependencies

- crewai: Framework for creating and orchestrating AI agent workflows
- crewai_tools: Collection of tools for CrewAI agents

## Future Enhancements

- Support for multiple YouTube channels
- Content customization options
- Image and media extraction
- Topic suggestion based on trending videos
- Multiple output formats (Markdown, HTML, etc.)

## License

[Your License Here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
