# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectVpcSync:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_channel_id': 'str',
        'instance_ids': 'list[str]',
        'force_sync': 'bool'
    }

    attribute_map = {
        'vpc_channel_id': 'vpc_channel_id',
        'instance_ids': 'instance_ids',
        'force_sync': 'force_sync'
    }

    def __init__(self, vpc_channel_id=None, instance_ids=None, force_sync=None):
        r"""ProjectVpcSync

        The model defined in huaweicloud sdk

        :param vpc_channel_id: VPC通道编号
        :type vpc_channel_id: str
        :param instance_ids: 新增关联的实例列表
        :type instance_ids: list[str]
        :param force_sync: 是否强制同步，默认不强制同步
        :type force_sync: bool
        """
        
        

        self._vpc_channel_id = None
        self._instance_ids = None
        self._force_sync = None
        self.discriminator = None

        if vpc_channel_id is not None:
            self.vpc_channel_id = vpc_channel_id
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if force_sync is not None:
            self.force_sync = force_sync

    @property
    def vpc_channel_id(self):
        r"""Gets the vpc_channel_id of this ProjectVpcSync.

        VPC通道编号

        :return: The vpc_channel_id of this ProjectVpcSync.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        r"""Sets the vpc_channel_id of this ProjectVpcSync.

        VPC通道编号

        :param vpc_channel_id: The vpc_channel_id of this ProjectVpcSync.
        :type vpc_channel_id: str
        """
        self._vpc_channel_id = vpc_channel_id

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this ProjectVpcSync.

        新增关联的实例列表

        :return: The instance_ids of this ProjectVpcSync.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this ProjectVpcSync.

        新增关联的实例列表

        :param instance_ids: The instance_ids of this ProjectVpcSync.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def force_sync(self):
        r"""Gets the force_sync of this ProjectVpcSync.

        是否强制同步，默认不强制同步

        :return: The force_sync of this ProjectVpcSync.
        :rtype: bool
        """
        return self._force_sync

    @force_sync.setter
    def force_sync(self, force_sync):
        r"""Sets the force_sync of this ProjectVpcSync.

        是否强制同步，默认不强制同步

        :param force_sync: The force_sync of this ProjectVpcSync.
        :type force_sync: bool
        """
        self._force_sync = force_sync

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
        if not isinstance(other, ProjectVpcSync):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
