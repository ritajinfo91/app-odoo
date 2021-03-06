# -*- coding: utf-8 -*-

# Created on 2017-11-05
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:


{
    'name': "App stock picking type group,库存作业类型分组",
    'version': '11.0.3.24',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    广州尚鹏，Sunpop.cn 的odoo模块。用于将库存作业分组，UI更方便。
    """,
    'description': """
    模块开发模板，目录结构与文件定义。
    """,
    'pre_init_hook': 'pre_init_hook',
    'depends': ['stock'],
    'images': ['static/description/demo1.jpg'],
    # 'currency': 'EUR',
    # 'price': 38,
    'data': [
        'views/stock_picking_type_group_views.xml',
        'views/stock_picking_type_views.xml',
        'data/stock_data.yml'
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'js': [
    ],
    'images': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
