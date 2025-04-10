# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTagStatusResponse(SdkResponse):

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
        'default_tags_enable': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'default_tags_enable': 'default_tags_enable'
    }

    def __init__(self, status=None, default_tags_enable=None):
        r"""ShowTagStatusResponse

        The model defined in huaweicloud sdk

        :param status: 标签处理状态
        :type status: str
        :param default_tags_enable: 默认标签是否已开启
        :type default_tags_enable: bool
        """
        
        super(ShowTagStatusResponse, self).__init__()

        self._status = None
        self._default_tags_enable = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if default_tags_enable is not None:
            self.default_tags_enable = default_tags_enable

    @property
    def status(self):
        r"""Gets the status of this ShowTagStatusResponse.

        标签处理状态

        :return: The status of this ShowTagStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTagStatusResponse.

        标签处理状态

        :param status: The status of this ShowTagStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def default_tags_enable(self):
        r"""Gets the default_tags_enable of this ShowTagStatusResponse.

        默认标签是否已开启

        :return: The default_tags_enable of this ShowTagStatusResponse.
        :rtype: bool
        """
        return self._default_tags_enable

    @default_tags_enable.setter
    def default_tags_enable(self, default_tags_enable):
        r"""Sets the default_tags_enable of this ShowTagStatusResponse.

        默认标签是否已开启

        :param default_tags_enable: The default_tags_enable of this ShowTagStatusResponse.
        :type default_tags_enable: bool
        """
        self._default_tags_enable = default_tags_enable

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
        if not isinstance(other, ShowTagStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
