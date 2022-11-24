# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMyActionTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'created_at': 'str',
        'func_pkg_path': 'str',
        'func_logo_path': 'dict(str, str)',
        'func_help_path': 'dict(str, str)',
        'func_test_report_path': 'dict(str, str)',
        'func_opensource_notice_path': 'dict(str, str)',
        'func_sla_path': 'dict(str, str)',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'template_name': 'template_name',
        'created_at': 'created_at',
        'func_pkg_path': 'func_pkg_path',
        'func_logo_path': 'func_logo_path',
        'func_help_path': 'func_help_path',
        'func_test_report_path': 'func_test_report_path',
        'func_opensource_notice_path': 'func_opensource_notice_path',
        'func_sla_path': 'func_sla_path',
        'x_request_id': 'X-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, template_name=None, created_at=None, func_pkg_path=None, func_logo_path=None, func_help_path=None, func_test_report_path=None, func_opensource_notice_path=None, func_sla_path=None, x_request_id=None, connection=None, content_length=None, date=None):
        """CreateMyActionTemplateResponse

        The model defined in huaweicloud sdk

        :param template_name: 三方算子ID
        :type template_name: str
        :param created_at: 三方算子创建的时间
        :type created_at: str
        :param func_pkg_path: 签名OBS地址，用于上传中英文算子包
        :type func_pkg_path: str
        :param func_logo_path: 签名OBS地址，用于上传中英文算子logo
        :type func_logo_path: dict(str, str)
        :param func_help_path: 签名OBS地址，用于上传中英文算子帮助文档
        :type func_help_path: dict(str, str)
        :param func_test_report_path: 签名OBS地址，用于上传中英文算子测试报告
        :type func_test_report_path: dict(str, str)
        :param func_opensource_notice_path: 签名OBS地址，用于上传中英文开源须知
        :type func_opensource_notice_path: dict(str, str)
        :param func_sla_path: 签名OBS地址，用于上传中英文服务协议材料
        :type func_sla_path: dict(str, str)
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(CreateMyActionTemplateResponse, self).__init__()

        self._template_name = None
        self._created_at = None
        self._func_pkg_path = None
        self._func_logo_path = None
        self._func_help_path = None
        self._func_test_report_path = None
        self._func_opensource_notice_path = None
        self._func_sla_path = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if template_name is not None:
            self.template_name = template_name
        if created_at is not None:
            self.created_at = created_at
        if func_pkg_path is not None:
            self.func_pkg_path = func_pkg_path
        if func_logo_path is not None:
            self.func_logo_path = func_logo_path
        if func_help_path is not None:
            self.func_help_path = func_help_path
        if func_test_report_path is not None:
            self.func_test_report_path = func_test_report_path
        if func_opensource_notice_path is not None:
            self.func_opensource_notice_path = func_opensource_notice_path
        if func_sla_path is not None:
            self.func_sla_path = func_sla_path
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def template_name(self):
        """Gets the template_name of this CreateMyActionTemplateResponse.

        三方算子ID

        :return: The template_name of this CreateMyActionTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this CreateMyActionTemplateResponse.

        三方算子ID

        :param template_name: The template_name of this CreateMyActionTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def created_at(self):
        """Gets the created_at of this CreateMyActionTemplateResponse.

        三方算子创建的时间

        :return: The created_at of this CreateMyActionTemplateResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateMyActionTemplateResponse.

        三方算子创建的时间

        :param created_at: The created_at of this CreateMyActionTemplateResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def func_pkg_path(self):
        """Gets the func_pkg_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文算子包

        :return: The func_pkg_path of this CreateMyActionTemplateResponse.
        :rtype: str
        """
        return self._func_pkg_path

    @func_pkg_path.setter
    def func_pkg_path(self, func_pkg_path):
        """Sets the func_pkg_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文算子包

        :param func_pkg_path: The func_pkg_path of this CreateMyActionTemplateResponse.
        :type func_pkg_path: str
        """
        self._func_pkg_path = func_pkg_path

    @property
    def func_logo_path(self):
        """Gets the func_logo_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文算子logo

        :return: The func_logo_path of this CreateMyActionTemplateResponse.
        :rtype: dict(str, str)
        """
        return self._func_logo_path

    @func_logo_path.setter
    def func_logo_path(self, func_logo_path):
        """Sets the func_logo_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文算子logo

        :param func_logo_path: The func_logo_path of this CreateMyActionTemplateResponse.
        :type func_logo_path: dict(str, str)
        """
        self._func_logo_path = func_logo_path

    @property
    def func_help_path(self):
        """Gets the func_help_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文算子帮助文档

        :return: The func_help_path of this CreateMyActionTemplateResponse.
        :rtype: dict(str, str)
        """
        return self._func_help_path

    @func_help_path.setter
    def func_help_path(self, func_help_path):
        """Sets the func_help_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文算子帮助文档

        :param func_help_path: The func_help_path of this CreateMyActionTemplateResponse.
        :type func_help_path: dict(str, str)
        """
        self._func_help_path = func_help_path

    @property
    def func_test_report_path(self):
        """Gets the func_test_report_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文算子测试报告

        :return: The func_test_report_path of this CreateMyActionTemplateResponse.
        :rtype: dict(str, str)
        """
        return self._func_test_report_path

    @func_test_report_path.setter
    def func_test_report_path(self, func_test_report_path):
        """Sets the func_test_report_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文算子测试报告

        :param func_test_report_path: The func_test_report_path of this CreateMyActionTemplateResponse.
        :type func_test_report_path: dict(str, str)
        """
        self._func_test_report_path = func_test_report_path

    @property
    def func_opensource_notice_path(self):
        """Gets the func_opensource_notice_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文开源须知

        :return: The func_opensource_notice_path of this CreateMyActionTemplateResponse.
        :rtype: dict(str, str)
        """
        return self._func_opensource_notice_path

    @func_opensource_notice_path.setter
    def func_opensource_notice_path(self, func_opensource_notice_path):
        """Sets the func_opensource_notice_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文开源须知

        :param func_opensource_notice_path: The func_opensource_notice_path of this CreateMyActionTemplateResponse.
        :type func_opensource_notice_path: dict(str, str)
        """
        self._func_opensource_notice_path = func_opensource_notice_path

    @property
    def func_sla_path(self):
        """Gets the func_sla_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文服务协议材料

        :return: The func_sla_path of this CreateMyActionTemplateResponse.
        :rtype: dict(str, str)
        """
        return self._func_sla_path

    @func_sla_path.setter
    def func_sla_path(self, func_sla_path):
        """Sets the func_sla_path of this CreateMyActionTemplateResponse.

        签名OBS地址，用于上传中英文服务协议材料

        :param func_sla_path: The func_sla_path of this CreateMyActionTemplateResponse.
        :type func_sla_path: dict(str, str)
        """
        self._func_sla_path = func_sla_path

    @property
    def x_request_id(self):
        """Gets the x_request_id of this CreateMyActionTemplateResponse.

        :return: The x_request_id of this CreateMyActionTemplateResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this CreateMyActionTemplateResponse.

        :param x_request_id: The x_request_id of this CreateMyActionTemplateResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this CreateMyActionTemplateResponse.

        :return: The connection of this CreateMyActionTemplateResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this CreateMyActionTemplateResponse.

        :param connection: The connection of this CreateMyActionTemplateResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this CreateMyActionTemplateResponse.

        :return: The content_length of this CreateMyActionTemplateResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this CreateMyActionTemplateResponse.

        :param content_length: The content_length of this CreateMyActionTemplateResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this CreateMyActionTemplateResponse.

        :return: The date of this CreateMyActionTemplateResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this CreateMyActionTemplateResponse.

        :param date: The date of this CreateMyActionTemplateResponse.
        :type date: str
        """
        self._date = date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateMyActionTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
