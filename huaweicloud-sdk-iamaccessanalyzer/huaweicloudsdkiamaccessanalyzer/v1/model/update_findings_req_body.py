# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFindingsReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'resource_urn': 'str',
        'status': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'resource_urn': 'resource_urn',
        'status': 'status'
    }

    def __init__(self, ids=None, resource_urn=None, status=None):
        r"""UpdateFindingsReqBody

        The model defined in huaweicloud sdk

        :param ids: 要更新的访问分析结果唯一标识符数组。
        :type ids: list[str]
        :param resource_urn: 资源的唯一资源标识符。
        :type resource_urn: str
        :param status: 要更新的访问分析结果状态。
        :type status: str
        """
        
        

        self._ids = None
        self._resource_urn = None
        self._status = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if resource_urn is not None:
            self.resource_urn = resource_urn
        self.status = status

    @property
    def ids(self):
        r"""Gets the ids of this UpdateFindingsReqBody.

        要更新的访问分析结果唯一标识符数组。

        :return: The ids of this UpdateFindingsReqBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this UpdateFindingsReqBody.

        要更新的访问分析结果唯一标识符数组。

        :param ids: The ids of this UpdateFindingsReqBody.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def resource_urn(self):
        r"""Gets the resource_urn of this UpdateFindingsReqBody.

        资源的唯一资源标识符。

        :return: The resource_urn of this UpdateFindingsReqBody.
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        r"""Sets the resource_urn of this UpdateFindingsReqBody.

        资源的唯一资源标识符。

        :param resource_urn: The resource_urn of this UpdateFindingsReqBody.
        :type resource_urn: str
        """
        self._resource_urn = resource_urn

    @property
    def status(self):
        r"""Gets the status of this UpdateFindingsReqBody.

        要更新的访问分析结果状态。

        :return: The status of this UpdateFindingsReqBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateFindingsReqBody.

        要更新的访问分析结果状态。

        :param status: The status of this UpdateFindingsReqBody.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, UpdateFindingsReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
