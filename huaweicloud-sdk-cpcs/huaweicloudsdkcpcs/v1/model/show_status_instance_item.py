# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatusInstanceItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_list': 'list[ShowStatusInstanceItemInstanceList]',
        'timestamp': 'int'
    }

    attribute_map = {
        'instance_list': 'instance_list',
        'timestamp': 'timestamp'
    }

    def __init__(self, instance_list=None, timestamp=None):
        r"""ShowStatusInstanceItem

        The model defined in huaweicloud sdk

        :param instance_list: 实例列表
        :type instance_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItemInstanceList`]
        :param timestamp: 采集时间，UNIX时间戳，单位毫秒
        :type timestamp: int
        """
        
        

        self._instance_list = None
        self._timestamp = None
        self.discriminator = None

        if instance_list is not None:
            self.instance_list = instance_list
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def instance_list(self):
        r"""Gets the instance_list of this ShowStatusInstanceItem.

        实例列表

        :return: The instance_list of this ShowStatusInstanceItem.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItemInstanceList`]
        """
        return self._instance_list

    @instance_list.setter
    def instance_list(self, instance_list):
        r"""Sets the instance_list of this ShowStatusInstanceItem.

        实例列表

        :param instance_list: The instance_list of this ShowStatusInstanceItem.
        :type instance_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItemInstanceList`]
        """
        self._instance_list = instance_list

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ShowStatusInstanceItem.

        采集时间，UNIX时间戳，单位毫秒

        :return: The timestamp of this ShowStatusInstanceItem.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ShowStatusInstanceItem.

        采集时间，UNIX时间戳，单位毫秒

        :param timestamp: The timestamp of this ShowStatusInstanceItem.
        :type timestamp: int
        """
        self._timestamp = timestamp

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowStatusInstanceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
