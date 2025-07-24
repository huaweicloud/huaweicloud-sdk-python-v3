# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExportProgressRequest:

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
        'async_job_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'async_job_id': 'async_job_id'
    }

    def __init__(self, x_language=None, async_job_id=None):
        r"""ShowExportProgressRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param async_job_id: 导出创建模板接口返回的异步ID。
        :type async_job_id: str
        """
        
        

        self._x_language = None
        self._async_job_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.async_job_id = async_job_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowExportProgressRequest.

        请求语言类型。

        :return: The x_language of this ShowExportProgressRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowExportProgressRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowExportProgressRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def async_job_id(self):
        r"""Gets the async_job_id of this ShowExportProgressRequest.

        导出创建模板接口返回的异步ID。

        :return: The async_job_id of this ShowExportProgressRequest.
        :rtype: str
        """
        return self._async_job_id

    @async_job_id.setter
    def async_job_id(self, async_job_id):
        r"""Sets the async_job_id of this ShowExportProgressRequest.

        导出创建模板接口返回的异步ID。

        :param async_job_id: The async_job_id of this ShowExportProgressRequest.
        :type async_job_id: str
        """
        self._async_job_id = async_job_id

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
        if not isinstance(other, ShowExportProgressRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
