# 🎓 MUST Exam Downloader

A powerful Python script for downloading exam papers from Meru University of Science and Technology (MUST). This tool allows students and faculty to efficiently scrape and organize exam papers from all schools within the university.

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 🚀 Features

- **Multi-School Support**: Download exams from all 9 schools/faculties at MUST
- **Selective Downloading**: Choose specific schools, unit codes, and years
- **Fast Downloads**: Multi-threaded downloading with 32 concurrent threads
- **Smart Organization**: Automatically creates organized folder structures
- **Duplicate Prevention**: Skips already downloaded files
- **Year Filtering**: Download exams from specific years (2014-2024) or all years
- **Unit Code Filtering**: Target specific subjects using unit codes
- **Progress Logging**: Real-time download progress and statistics

## 🏫 Supported Schools

| Code | School Name |
|------|-------------|
| SAFS | School of Agriculture and Food Sciences |
| SBE  | School of Business and Economics |
| SCI  | School of Computing and Informatics |
| SEA  | School of Engineering and Architecture |
| SED  | School of Education |
| SHS  | School of Health Sciences |
| SON  | School of Nursing |
| SPAS | School of Pure and Applied Sciences |
| TVET | Technical and Vocational Education Training |

## 📋 Prerequisites

- Python 3.6 or higher
- Internet connection
- Required Python packages (see Installation)

## 🔧 Installation

1. **Clone or download the script**
   ```bash
   # clone https://github.com/derksKCodes/MUST-Exam-Downloader.git to your desired directory
   ```

2. **Install required packages**
   ```bash
   pip install requests
   ```

3. **Make the script executable** (Optional on Unix systems)
   ```bash
   chmod +x examdownloader.py
   ```

## 🎯 Usage

1. **Run the script**
   ```bash
   python examdownloader.py
   ```

2. **Follow the interactive prompts:**

   - **Select Schools**: Choose one or more schools by entering their index numbers (space-separated)
     ```
     Example: 0 2 4  (selects SAFS, SCI, and SED)
     ```

   - **Enter Unit Codes**: Specify the subjects you want to download
     ```
     Example: SMA-3300 BBS-3475 CIT-3476
     ```

   - **Select Years**: Choose specific years or 'all' for all available years
     ```
     Example: 2022 2023 2024  or  all
     ```

## 📁 Output Structure

The script creates an organized folder structure:

```
exams/
├── safs/
│   ├── 2022/
│   ├── 2023/
│   └── 2024/
├── sbe/
│   ├── 2022/
│   └── 2023/
└── sci/
    ├── 2021/
    ├── 2022/
    └── 2023/
```

## 💡 Example Usage

```bash
# Run the script
python examdownloader.py

# Example interaction:
# Select schools: 0 2 4
# Unit codes: SMA-3300 CCS-3325 BBS-3475
# Years: 2022 2023 2024
```

## 🔍 Common Unit Codes

Here are some example unit codes you might use:

- **Mathematics**: SMA-3300, SMA-3400, SMA-3404, SMA-3405
- **Computer Science**: CCS-3325, CIT-3476
- **Business**: BBS-3475

## ⚙️ Configuration

### Thread Count
The script uses 32 threads by default. You can modify this by changing the `THREAD_C` variable:

```python
THREAD_C = 16  # Reduce for slower connections
```

### Years Range
To modify the available years, update the years list in the script:

```python
years = ["2020", "2021", "2022", "2023", "2024"]
```

## 🚨 Important Notes

- **Respectful Usage**: The script includes warnings about making too many requests simultaneously
- **SSL Warnings**: SSL certificate warnings are suppressed for the university website
- **File Overwriting**: The script asks before overwriting existing directories
- **Network Dependency**: Requires stable internet connection for optimal performance

## 🛠️ Troubleshooting

### Common Issues

1. **Connection Errors**
   - Check your internet connection
   - Verify the university website is accessible

2. **Permission Errors**
   - Ensure you have write permissions in the script directory
   - Run with appropriate privileges if needed

3. **Invalid School Index**
   - Enter valid numbers (0-8) corresponding to the schools
   - Use space-separated values for multiple schools

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. Please respect the university's terms of service and use responsibly. The authors are not responsible for any misuse of this software.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the code comments for additional details
3. Create an issue with detailed information about your problem

---

**Happy Learning! 🎓**

*Made with ❤️ for MUST students*
```

