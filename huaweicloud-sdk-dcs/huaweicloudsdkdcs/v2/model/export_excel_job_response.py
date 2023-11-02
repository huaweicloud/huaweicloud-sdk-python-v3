# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportExcelJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'file_name': 'str',
        'link': 'str',
        'err_code': 'str',
        'err_msg': 'str'
    }

    attribute_map = {
        'status': 'status',
        'file_name': 'file_name',
        'link': 'link',
        'err_code': 'err_code',
        'err_msg': 'err_msg'
    }

    def __init__(self, status=None, file_name=None, link=None, err_code=None, err_msg=None):
        """ExportExcelJobResponse

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: str
        :param file_name: 文件名
        :type file_name: str
        :param link: 链接
        :type link: str
        :param err_code: 错误码
        :type err_code: str
        :param err_msg: 错误信息
        :type err_msg: str
        """
        
        super(ExportExcelJobResponse, self).__init__()

        self._status = None
        self._file_name = None
        self._link = None
        self._err_code = None
        self._err_msg = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if file_name is not None:
            self.file_name = file_name
        if link is not None:
            self.link = link
        if err_code is not None:
            self.err_code = err_code
        if err_msg is not None:
            self.err_msg = err_msg

    @property
    def status(self):
        """Gets the status of this ExportExcelJobResponse.

        状态

        :return: The status of this ExportExcelJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExportExcelJobResponse.

        状态

        :param status: The status of this ExportExcelJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def file_name(self):
        """Gets the file_name of this ExportExcelJobResponse.

        文件名

        :return: The file_name of this ExportExcelJobResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ExportExcelJobResponse.

        文件名

        :param file_name: The file_name of this ExportExcelJobResponse.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def link(self):
        """Gets the link of this ExportExcelJobResponse.

        链接

        :return: The link of this ExportExcelJobResponse.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ExportExcelJobResponse.

        链接

        :param link: The link of this ExportExcelJobResponse.
        :type link: str
        """
        self._link = link

    @property
    def err_code(self):
        """Gets the err_code of this ExportExcelJobResponse.

        错误码

        :return: The err_code of this ExportExcelJobResponse.
        :rtype: str
        """
        return self._err_code

    @err_code.setter
    def err_code(self, err_code):
        """Sets the err_code of this ExportExcelJobResponse.

        错误码

        :param err_code: The err_code of this ExportExcelJobResponse.
        :type err_code: str
        """
        self._err_code = err_code

    @property
    def err_msg(self):
        """Gets the err_msg of this ExportExcelJobResponse.

        错误信息

        :return: The err_msg of this ExportExcelJobResponse.
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        """Sets the err_msg of this ExportExcelJobResponse.

        错误信息

        :param err_msg: The err_msg of this ExportExcelJobResponse.
        :type err_msg: str
        """
        self._err_msg = err_msg

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
        if not isinstance(other, ExportExcelJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
