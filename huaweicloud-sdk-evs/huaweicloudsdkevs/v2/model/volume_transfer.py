# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeTransfer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'id': 'str',
        'links': 'list[Link]',
        'name': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'id': 'id',
        'links': 'links',
        'name': 'name',
        'volume_id': 'volume_id'
    }

    def __init__(self, created_at=None, id=None, links=None, name=None, volume_id=None):
        """VolumeTransfer

        The model defined in huaweicloud sdk

        :param created_at: 云硬盘过户记录的创建时间。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX
        :type created_at: str
        :param id: 云硬盘过户记录的ID。
        :type id: str
        :param links: 云硬盘过户记录的链接。
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        :param name: 云硬盘过户记录的名称。
        :type name: str
        :param volume_id: 云硬盘ID。
        :type volume_id: str
        """
        
        

        self._created_at = None
        self._id = None
        self._links = None
        self._name = None
        self._volume_id = None
        self.discriminator = None

        self.created_at = created_at
        self.id = id
        self.links = links
        self.name = name
        self.volume_id = volume_id

    @property
    def created_at(self):
        """Gets the created_at of this VolumeTransfer.

        云硬盘过户记录的创建时间。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The created_at of this VolumeTransfer.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VolumeTransfer.

        云硬盘过户记录的创建时间。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param created_at: The created_at of this VolumeTransfer.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this VolumeTransfer.

        云硬盘过户记录的ID。

        :return: The id of this VolumeTransfer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeTransfer.

        云硬盘过户记录的ID。

        :param id: The id of this VolumeTransfer.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this VolumeTransfer.

        云硬盘过户记录的链接。

        :return: The links of this VolumeTransfer.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VolumeTransfer.

        云硬盘过户记录的链接。

        :param links: The links of this VolumeTransfer.
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        self._links = links

    @property
    def name(self):
        """Gets the name of this VolumeTransfer.

        云硬盘过户记录的名称。

        :return: The name of this VolumeTransfer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeTransfer.

        云硬盘过户记录的名称。

        :param name: The name of this VolumeTransfer.
        :type name: str
        """
        self._name = name

    @property
    def volume_id(self):
        """Gets the volume_id of this VolumeTransfer.

        云硬盘ID。

        :return: The volume_id of this VolumeTransfer.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this VolumeTransfer.

        云硬盘ID。

        :param volume_id: The volume_id of this VolumeTransfer.
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
        if not isinstance(other, VolumeTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
