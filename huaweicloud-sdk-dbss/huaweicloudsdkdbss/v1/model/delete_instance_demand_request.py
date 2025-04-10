# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInstanceDemandRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'delete_publicip': 'bool',
        'delete_volume': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'delete_publicip': 'delete_publicip',
        'delete_volume': 'delete_volume'
    }

    def __init__(self, id=None, delete_publicip=None, delete_volume=None):
        r"""DeleteInstanceDemandRequest

        The model defined in huaweicloud sdk

        :param id: 实例ID。可在查询实例列表接口的ID字段获取。
        :type id: str
        :param delete_publicip: 是否删除弹性IP
        :type delete_publicip: bool
        :param delete_volume: 是否删除磁盘
        :type delete_volume: bool
        """
        
        

        self._id = None
        self._delete_publicip = None
        self._delete_volume = None
        self.discriminator = None

        self.id = id
        if delete_publicip is not None:
            self.delete_publicip = delete_publicip
        if delete_volume is not None:
            self.delete_volume = delete_volume

    @property
    def id(self):
        r"""Gets the id of this DeleteInstanceDemandRequest.

        实例ID。可在查询实例列表接口的ID字段获取。

        :return: The id of this DeleteInstanceDemandRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteInstanceDemandRequest.

        实例ID。可在查询实例列表接口的ID字段获取。

        :param id: The id of this DeleteInstanceDemandRequest.
        :type id: str
        """
        self._id = id

    @property
    def delete_publicip(self):
        r"""Gets the delete_publicip of this DeleteInstanceDemandRequest.

        是否删除弹性IP

        :return: The delete_publicip of this DeleteInstanceDemandRequest.
        :rtype: bool
        """
        return self._delete_publicip

    @delete_publicip.setter
    def delete_publicip(self, delete_publicip):
        r"""Sets the delete_publicip of this DeleteInstanceDemandRequest.

        是否删除弹性IP

        :param delete_publicip: The delete_publicip of this DeleteInstanceDemandRequest.
        :type delete_publicip: bool
        """
        self._delete_publicip = delete_publicip

    @property
    def delete_volume(self):
        r"""Gets the delete_volume of this DeleteInstanceDemandRequest.

        是否删除磁盘

        :return: The delete_volume of this DeleteInstanceDemandRequest.
        :rtype: bool
        """
        return self._delete_volume

    @delete_volume.setter
    def delete_volume(self, delete_volume):
        r"""Sets the delete_volume of this DeleteInstanceDemandRequest.

        是否删除磁盘

        :param delete_volume: The delete_volume of this DeleteInstanceDemandRequest.
        :type delete_volume: bool
        """
        self._delete_volume = delete_volume

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
        if not isinstance(other, DeleteInstanceDemandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
