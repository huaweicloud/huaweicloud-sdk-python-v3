# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceSnapshotView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'description': 'str',
        'instance_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'description': 'description',
        'instance_id': 'instance_id',
        'version': 'version'
    }

    def __init__(self, create_time=None, description=None, instance_id=None, version=None):
        """InstanceSnapshotView

        The model defined in huaweicloud sdk

        :param create_time: 创建时间。
        :type create_time: int
        :param description: 描述。
        :type description: str
        :param instance_id: 应用组件实例ID。
        :type instance_id: str
        :param version: 版本号。
        :type version: str
        """
        
        

        self._create_time = None
        self._description = None
        self._instance_id = None
        self._version = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if instance_id is not None:
            self.instance_id = instance_id
        if version is not None:
            self.version = version

    @property
    def create_time(self):
        """Gets the create_time of this InstanceSnapshotView.

        创建时间。

        :return: The create_time of this InstanceSnapshotView.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InstanceSnapshotView.

        创建时间。

        :param create_time: The create_time of this InstanceSnapshotView.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this InstanceSnapshotView.

        描述。

        :return: The description of this InstanceSnapshotView.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceSnapshotView.

        描述。

        :param description: The description of this InstanceSnapshotView.
        :type description: str
        """
        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceSnapshotView.

        应用组件实例ID。

        :return: The instance_id of this InstanceSnapshotView.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceSnapshotView.

        应用组件实例ID。

        :param instance_id: The instance_id of this InstanceSnapshotView.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def version(self):
        """Gets the version of this InstanceSnapshotView.

        版本号。

        :return: The version of this InstanceSnapshotView.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstanceSnapshotView.

        版本号。

        :param version: The version of this InstanceSnapshotView.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, InstanceSnapshotView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
