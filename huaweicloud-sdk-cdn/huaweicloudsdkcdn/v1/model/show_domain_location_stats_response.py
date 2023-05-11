# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainLocationStatsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_by': 'str',
        'result': 'dict(str, object)'
    }

    attribute_map = {
        'group_by': 'group_by',
        'result': 'result'
    }

    def __init__(self, group_by=None, result=None):
        """ShowDomainLocationStatsResponse

        The model defined in huaweicloud sdk

        :param group_by: 数据分组方式
        :type group_by: str
        :param result: 按指定的分组方式组织的数据
        :type result: dict(str, object)
        """
        
        super(ShowDomainLocationStatsResponse, self).__init__()

        self._group_by = None
        self._result = None
        self.discriminator = None

        if group_by is not None:
            self.group_by = group_by
        if result is not None:
            self.result = result

    @property
    def group_by(self):
        """Gets the group_by of this ShowDomainLocationStatsResponse.

        数据分组方式

        :return: The group_by of this ShowDomainLocationStatsResponse.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ShowDomainLocationStatsResponse.

        数据分组方式

        :param group_by: The group_by of this ShowDomainLocationStatsResponse.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def result(self):
        """Gets the result of this ShowDomainLocationStatsResponse.

        按指定的分组方式组织的数据

        :return: The result of this ShowDomainLocationStatsResponse.
        :rtype: dict(str, object)
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowDomainLocationStatsResponse.

        按指定的分组方式组织的数据

        :param result: The result of this ShowDomainLocationStatsResponse.
        :type result: dict(str, object)
        """
        self._result = result

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
        if not isinstance(other, ShowDomainLocationStatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
