# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeTransferSummary:

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
        'links': 'list[Link]',
        'name': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'name': 'name',
        'volume_id': 'volume_id'
    }

    def __init__(self, id=None, links=None, name=None, volume_id=None):
        """VolumeTransferSummary

        The model defined in huaweicloud sdk

        :param id: 云硬盘过户记录的ID。
        :type id: str
        :param links: 云硬盘过户记录的链接
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        :param name: 云硬盘过户记录的名称
        :type name: str
        :param volume_id: 云硬盘ID。
        :type volume_id: str
        """
        
        

        self._id = None
        self._links = None
        self._name = None
        self._volume_id = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.name = name
        self.volume_id = volume_id

    @property
    def id(self):
        """Gets the id of this VolumeTransferSummary.

        云硬盘过户记录的ID。

        :return: The id of this VolumeTransferSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeTransferSummary.

        云硬盘过户记录的ID。

        :param id: The id of this VolumeTransferSummary.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this VolumeTransferSummary.

        云硬盘过户记录的链接

        :return: The links of this VolumeTransferSummary.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VolumeTransferSummary.

        云硬盘过户记录的链接

        :param links: The links of this VolumeTransferSummary.
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        self._links = links

    @property
    def name(self):
        """Gets the name of this VolumeTransferSummary.

        云硬盘过户记录的名称

        :return: The name of this VolumeTransferSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeTransferSummary.

        云硬盘过户记录的名称

        :param name: The name of this VolumeTransferSummary.
        :type name: str
        """
        self._name = name

    @property
    def volume_id(self):
        """Gets the volume_id of this VolumeTransferSummary.

        云硬盘ID。

        :return: The volume_id of this VolumeTransferSummary.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this VolumeTransferSummary.

        云硬盘ID。

        :param volume_id: The volume_id of this VolumeTransferSummary.
        :type volume_id: str
        """
        self._volume_id = volume_id

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
        if not isinstance(other, VolumeTransferSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
