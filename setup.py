from setuptools import setup

setup(
    name='codechan',
    version='0.1.0',
    description='4chan for coders',
    url='https://github.com/devops-sdu-2020/ca-project',
    author='Emil Tang Kristensen',
    author_email='emiltangkristen@gmail.com',
    license='BSD 2-clause',
    packages=['app'],
    install_requires=['click==7.1.2',
                      'Flask==1.1.2',
                      'Flask-SQLAlchemy==2.4.4',
                      'Flask-WTF==0.14.3',
                      'itsdangerous==1.1.0',
                      'Jinja2==2.11.2',
                      'MarkupSafe==1.1.1',
                      'SQLAlchemy==1.3.18',
                      'Werkzeug==1.0.1',
                      'WTForms==2.3.3'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
