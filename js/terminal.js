const output = document.getElementById('output');
const input = document.getElementById('command-input');
const terminal = document.getElementById('terminal');
const cursor = document.querySelector('.cursor');

let isTyping = false;
let commandHistory = [];
let historyIndex = -1;
let commandQueue = [];

const quotes = [
    "Code is like humor. When you have to explain it, it's bad.",
    "First, solve the problem. Then, write the code.",
    "The best error message is the one that never shows up.",
    "Testing leads to failure, and failure leads to understanding.",
    "A bug is never just a mistake. It's a learning opportunity.",
    "Write code that humans can read, not just machines.",
    "Quality is not an act, it is a habit.",
    "The only way to go fast is to go well."
];

const commands = {
    whoami: () => `Syefdi Fasmawi Syaban
19 years old, based in South Jakarta
Junior QA Tester & Informatics Engineering Student
Currently working at CV Gemilang Inti Teknologi`,

    about: () => `I'm a 19-year-old based in South Jakarta, currently working as a 
Junior QA Tester while studying Informatics Engineering at Universitas 
Pamulang on weekends.

My day-to-day involves testing enterprise web systems, writing bug reports, 
coordinating with developers, and occasionally fixing small issues on live 
systems. I've been involved in building a few of these systems too, mostly 
on the QA side but sometimes contributing to the code itself.

I take quality seriously, but I'm still early in my career and have a lot 
to learn. Right now I'm focused on getting better at what I do and picking 
up new skills along the way.`,

    skills: () => `[ Testing & QA ]
Functional Testing | Regression Testing | Bug Reporting
Web Application Testing | Dev-to-Prod Pipeline | Cross-browser Testing
Smoke Testing | Bug Lifecycle Management | Test Case Documentation

[ Tools & Workflow ]
Git | GitHub | VS Code | Google Workspace | Trello | Notion
Jira | Postman | Microsoft Office | Chrome DevTools

[ Currently Learning ]
SQL for Data Validation | Test Automation Fundamentals`,

    experience: () => `CV Gemilang Inti Teknologi
Role   : Junior QA Tester
Period : May 2025 - Present

Responsibilities:
- Tested 2-3 enterprise web systems simultaneously across parallel 
  development tracks, running functional and regression tests on 
  weekly release cycles
- Reported 100+ bugs over 3 months with detailed reproduction steps, 
  environment info, and screenshots
- Participated in weekly deployment cycles across multiple systems, 
  catching critical issues before each production release
- Fixed small issues directly on the live CRM system when needed
- Helped build a Document Management System from early stages
- Involved in the early development of an HRIS attendance app`,

    education: () => `Universitas Pamulang
Degree : S1 Informatics Engineering
Period : 2025 - Present
Status : Active Student

SMK Fajar Ciseeng
Major  : Computer & Network Engineering
Period : 2022 - 2025`,

    projects: () => `[01] ERM System - CV Gemilang Inti Teknologi
Role : QA, Build
Enterprise Resource Management system for internal business operations.
Tested two active versions simultaneously - ongoing revamp and production.
Link : erm.gemilangteknologi.com

[02] CRM System - CV Gemilang Inti Teknologi
Role : QA, Dev, Build
Customer Relationship Management platform for managing client data.
Handled QA testing, fixed issues on live system, helped with build process.
Link : crms.gemilangteknologi.com

[03] Document Management System - CV Gemilang Inti Teknologi
Role : Dev, Build
Web-based system for organizing and storing documents.
Contributed from early stages on both development and QA side.
Link : github.com/Syefdi/Document_Management_System

[04] HRIS / Attendance System - CV Gemilang Inti Teknologi
Role : QA, Dev
Attendance tracking app for employee management.
Joined during early development, did functional testing as features built.
Link : absensi.intipowerabadi.com

[05] PD System - CV Gemilang Inti Teknologi
Role : QA, Dev
Internal management dashboard built for PT Kencana Zavira.
Helped with minor development work and QA testing during build phase.
Link : pds.kencana-zavira.com

[06] Bug Report Management Tool - Personal Project
Role : Full Stack Developer
Web app for QA testers and developers to track and manage bug reports
with audit trail and role-based views.
Stack: Python, FastAPI, PostgreSQL, Tailwind CSS
Link : github.com/Syefdi/bugReport`,

    certifications: () => `[1] Spec-Driven Development dengan Kiro
Issuer : Dicoding x AWS - AWS AI Academy
Year   : 2026
Status : Completed
Verify : dicoding.com/certificates/JMZVOJKQ3XN9

[2] Prompt Engineering untuk Software Developer
Issuer : Dicoding
Year   : 2025
Status : Completed
Verify : dicoding.com/certificates/98XWOOW2LZM3

[3] Belajar Dasar Structured Query Language (SQL)
Issuer : Dicoding
Year   : 2025
Status : Completed
Verify : dicoding.com/certificates/1OP8041YQPQK

[4] Belajar Dasar Git dengan GitHub
Issuer : Dicoding
Year   : 2024
Status : Completed
Verify : dicoding.com/certificates/6RPNDK1WMPZ2

[5] Belajar Dasar Manajemen Proyek
Issuer : Dicoding
Year   : 2024
Status : Completed
Verify : dicoding.com/certificates/EYX4YV8E2ZDL`,

    contact: () => `Email    : syefdifasmawi@gmail.com
GitHub   : github.com/Syefdi
LinkedIn : linkedin.com/in/syefdi-fasmawi-syaban-6b6531337
Portfolio: syefdi.github.io`,

    cv: () => {
        downloadResume();
        return 'Downloading resume.pdf...';
    },

    help: () => `Available commands:

whoami          Who is Syefdi
about           Background and current status
skills          Technical skills and tools
experience      Work experience
education       Education background
projects        Personal and work projects
certifications  Courses and credentials
contact         Contact information
cv              Download resume
clear           Clear terminal
help            Show this help message

Type any command and press Enter.`,

    clear: () => {
        output.innerHTML = '';
        return null;
    },

    secret: () => `You found it. Here is the truth:
I build things because I refuse to be replaced by the tools I use.`,

    sudo: () => `Permission denied. Nice try though.`,

    'rm -rf /': () => `Seriously? Not today. Everything is fine.`,

    'rm -rf': () => `Seriously? Not today. Everything is fine.`,

    matrix: () => {
        triggerMatrixEffect();
        return null;
    },

    quote: () => {
        return quotes[Math.floor(Math.random() * quotes.length)];
    }
};

function addLine(text, className = '') {
    const line = document.createElement('div');
    line.className = `output-line ${className}`;
    line.textContent = text;
    output.appendChild(line);
}

function addCommandLine(command) {
    const line = document.createElement('div');
    line.className = 'command-line';
    line.innerHTML = `<span class="prompt">syefdi@portfolio:~$</span> ${command}`;
    output.appendChild(line);
}

async function typeText(text) {
    isTyping = true;
    hideInputLine();
    
    const lines = text.split('\n');
    
    for (let i = 0; i < lines.length; i++) {
        const line = document.createElement('div');
        line.className = 'output-line';
        output.appendChild(line);
        
        const chars = lines[i].split('');
        for (let j = 0; j < chars.length; j++) {
            await sleep(25);
            line.textContent += chars[j];
            if (j % 5 === 0 || j === chars.length - 1) {
                scrollToBottom();
            }
        }
    }
    
    isTyping = false;
    showInputLine();
    scrollToBottom();
}

function hideInputLine() {
    const inputLine = document.querySelector('.input-line');
    if (inputLine) {
        inputLine.style.display = 'none';
    }
}

function showInputLine() {
    const inputLine = document.querySelector('.input-line');
    if (inputLine) {
        inputLine.style.display = 'flex';
    }
    input.focus();
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function scrollToBottom() {
    terminal.scrollTop = terminal.scrollHeight;
}

function updateCursor() {
    const value = input.value;
    const textWidth = getTextWidth(value);
    const promptElement = document.querySelector('.input-line .prompt');
    const promptWidth = promptElement ? promptElement.offsetWidth : 180;
    cursor.style.left = `${promptWidth + textWidth + 8}px`;
}

function getTextWidth(text) {
    const canvas = getTextWidth.canvas || (getTextWidth.canvas = document.createElement('canvas'));
    const context = canvas.getContext('2d');
    context.font = '14px "JetBrains Mono", monospace';
    return context.measureText(text).width;
}

function downloadResume() {
    const link = document.createElement('a');
    link.href = 'assets/documents/resume.pdf';
    link.download = 'Syefdi_Fasmawi_Syaban_Resume.pdf';
    link.click();
}

function triggerMatrixEffect() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()';
    const columns = Math.floor(terminal.offsetWidth / 12);
    
    for (let i = 0; i < columns; i++) {
        setTimeout(() => {
            const char = chars[Math.floor(Math.random() * chars.length)];
            const span = document.createElement('span');
            span.className = 'matrix-char';
            span.textContent = char;
            span.style.left = `${i * 12}px`;
            span.style.top = '0';
            terminal.appendChild(span);
            
            setTimeout(() => {
                terminal.removeChild(span);
            }, 3000);
        }, i * 50);
    }
}

async function executeCommand(cmd) {
    const trimmedCmd = cmd.trim();
    
    if (!trimmedCmd) return;
    
    commandQueue.push(trimmedCmd);
    
    if (isTyping) {
        return;
    }
    
    while (commandQueue.length > 0) {
        const command = commandQueue.shift();
        
        addCommandLine(command);
        
        if (!commandHistory.includes(command)) {
            commandHistory.unshift(command);
        }
        historyIndex = -1;
        
        const lowerCmd = command.toLowerCase();
        
        if (commands[lowerCmd]) {
            const result = commands[lowerCmd]();
            if (result !== null) {
                await typeText(result);
            }
        } else {
            await typeText(`command not found: ${command}. Type 'help' to see available commands.`);
        }
        
        scrollToBottom();
    }
}

async function init() {
    const welcomeMessage = `Welcome to Syefdi's Terminal Portfolio.
Type 'help' to see available commands.`;
    await typeText(welcomeMessage);
}

function autocomplete(partial) {
    const availableCommands = Object.keys(commands);
    const matches = availableCommands.filter(cmd => cmd.startsWith(partial.toLowerCase()));
    
    if (matches.length === 1) {
        return matches[0];
    } else if (matches.length > 1) {
        const commonPrefix = findCommonPrefix(matches);
        return commonPrefix || partial;
    }
    return partial;
}

function findCommonPrefix(strings) {
    if (strings.length === 0) return '';
    
    let prefix = strings[0];
    for (let i = 1; i < strings.length; i++) {
        while (strings[i].indexOf(prefix) !== 0) {
            prefix = prefix.slice(0, -1);
            if (prefix === '') return '';
        }
    }
    return prefix;
}

input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        const command = input.value;
        input.value = '';
        updateCursor();
        executeCommand(command);
    } else if (e.key === 'Tab') {
        e.preventDefault();
        const current = input.value.trim();
        if (current) {
            const completed = autocomplete(current);
            input.value = completed;
            updateCursor();
        }
    } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (historyIndex < commandHistory.length - 1) {
            historyIndex++;
            input.value = commandHistory[historyIndex];
            updateCursor();
        }
    } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (historyIndex > 0) {
            historyIndex--;
            input.value = commandHistory[historyIndex];
            updateCursor();
        } else if (historyIndex === 0) {
            historyIndex = -1;
            input.value = '';
            updateCursor();
        }
    }
});

input.addEventListener('input', updateCursor);

terminal.addEventListener('click', () => {
    input.focus();
});

document.addEventListener('DOMContentLoaded', () => {
    input.focus();
    updateCursor();
    init();
});
