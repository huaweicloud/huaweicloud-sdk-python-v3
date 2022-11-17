# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadDataTraceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'eihealth_project_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'eihealth_project_id': 'eihealth_project_id'
    }

    def __init__(self, x_language=None, eihealth_project_id=None):
        """DownloadDataTraceRequest

        The model defined in huaweicloud sdk

        :param x_language: Locale语言信息, zh_cn返回中文，en-us返回英文
        :type x_language: str
        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        """
        
        

        self._x_language = None
        self._eihealth_project_id = None
        self.discriminator = None

        self.x_language = x_language
        self.eihealth_project_id = eihealth_project_id

    @property
    def x_language(self):
        """Gets the x_language of this DownloadDataTraceRequest.

        Locale语言信息, zh_cn返回中文，en-us返回英文

        :return: The x_language of this DownloadDataTraceRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this DownloadDataTraceRequest.

        Locale语言信息, zh_cn返回中文，en-us返回英文

        :param x_language: The x_language of this DownloadDataTraceRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this DownloadDataTraceRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this DownloadDataTraceRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this DownloadDataTraceRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this DownloadDataTraceRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

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
        if not isinstance(other, DownloadDataTraceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
