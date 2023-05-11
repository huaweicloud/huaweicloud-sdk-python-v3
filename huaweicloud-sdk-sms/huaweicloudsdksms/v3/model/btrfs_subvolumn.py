# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BtrfsSubvolumn:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'is_snapshot': 'str',
        'subvol_id': 'str',
        'parent_id': 'str',
        'subvol_name': 'str',
        'subvol_mount_path': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'is_snapshot': 'is_snapshot',
        'subvol_id': 'subvol_id',
        'parent_id': 'parent_id',
        'subvol_name': 'subvol_name',
        'subvol_mount_path': 'subvol_mount_path'
    }

    def __init__(self, uuid=None, is_snapshot=None, subvol_id=None, parent_id=None, subvol_name=None, subvol_mount_path=None):
        """BtrfsSubvolumn

        The model defined in huaweicloud sdk

        :param uuid: 父卷的uuid
        :type uuid: str
        :param is_snapshot: 子卷是否为快照
        :type is_snapshot: str
        :param subvol_id: 子卷的ID
        :type subvol_id: str
        :param parent_id: 父卷ID
        :type parent_id: str
        :param subvol_name: 子卷的名称
        :type subvol_name: str
        :param subvol_mount_path: 子卷的挂载路径
        :type subvol_mount_path: str
        """
        
        

        self._uuid = None
        self._is_snapshot = None
        self._subvol_id = None
        self._parent_id = None
        self._subvol_name = None
        self._subvol_mount_path = None
        self.discriminator = None

        self.uuid = uuid
        self.is_snapshot = is_snapshot
        self.subvol_id = subvol_id
        self.parent_id = parent_id
        self.subvol_name = subvol_name
        self.subvol_mount_path = subvol_mount_path

    @property
    def uuid(self):
        """Gets the uuid of this BtrfsSubvolumn.

        父卷的uuid

        :return: The uuid of this BtrfsSubvolumn.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this BtrfsSubvolumn.

        父卷的uuid

        :param uuid: The uuid of this BtrfsSubvolumn.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def is_snapshot(self):
        """Gets the is_snapshot of this BtrfsSubvolumn.

        子卷是否为快照

        :return: The is_snapshot of this BtrfsSubvolumn.
        :rtype: str
        """
        return self._is_snapshot

    @is_snapshot.setter
    def is_snapshot(self, is_snapshot):
        """Sets the is_snapshot of this BtrfsSubvolumn.

        子卷是否为快照

        :param is_snapshot: The is_snapshot of this BtrfsSubvolumn.
        :type is_snapshot: str
        """
        self._is_snapshot = is_snapshot

    @property
    def subvol_id(self):
        """Gets the subvol_id of this BtrfsSubvolumn.

        子卷的ID

        :return: The subvol_id of this BtrfsSubvolumn.
        :rtype: str
        """
        return self._subvol_id

    @subvol_id.setter
    def subvol_id(self, subvol_id):
        """Sets the subvol_id of this BtrfsSubvolumn.

        子卷的ID

        :param subvol_id: The subvol_id of this BtrfsSubvolumn.
        :type subvol_id: str
        """
        self._subvol_id = subvol_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BtrfsSubvolumn.

        父卷ID

        :return: The parent_id of this BtrfsSubvolumn.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BtrfsSubvolumn.

        父卷ID

        :param parent_id: The parent_id of this BtrfsSubvolumn.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def subvol_name(self):
        """Gets the subvol_name of this BtrfsSubvolumn.

        子卷的名称

        :return: The subvol_name of this BtrfsSubvolumn.
        :rtype: str
        """
        return self._subvol_name

    @subvol_name.setter
    def subvol_name(self, subvol_name):
        """Sets the subvol_name of this BtrfsSubvolumn.

        子卷的名称

        :param subvol_name: The subvol_name of this BtrfsSubvolumn.
        :type subvol_name: str
        """
        self._subvol_name = subvol_name

    @property
    def subvol_mount_path(self):
        """Gets the subvol_mount_path of this BtrfsSubvolumn.

        子卷的挂载路径

        :return: The subvol_mount_path of this BtrfsSubvolumn.
        :rtype: str
        """
        return self._subvol_mount_path

    @subvol_mount_path.setter
    def subvol_mount_path(self, subvol_mount_path):
        """Sets the subvol_mount_path of this BtrfsSubvolumn.

        子卷的挂载路径

        :param subvol_mount_path: The subvol_mount_path of this BtrfsSubvolumn.
        :type subvol_mount_path: str
        """
        self._subvol_mount_path = subvol_mount_path

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
        if not isinstance(other, BtrfsSubvolumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
