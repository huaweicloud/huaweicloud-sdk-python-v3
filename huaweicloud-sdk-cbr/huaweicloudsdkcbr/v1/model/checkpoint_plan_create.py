# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointPlanCreate:

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
        'name': 'str',
        'resources': 'list[CheckpointResourceResp]',
        'skipped_resources': 'list[CheckpointCreateSkippedResource]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'resources': 'resources',
        'skipped_resources': 'skipped_resources'
    }

    def __init__(self, id=None, name=None, resources=None, skipped_resources=None):
        """CheckpointPlanCreate

        The model defined in huaweicloud sdk

        :param id: 存储库id
        :type id: str
        :param name: 存储库名称
        :type name: str
        :param resources: 备份对象
        :type resources: list[:class:`huaweicloudsdkcbr.v1.CheckpointResourceResp`]
        :param skipped_resources: 备份时跳过的资源列表
        :type skipped_resources: list[:class:`huaweicloudsdkcbr.v1.CheckpointCreateSkippedResource`]
        """
        
        

        self._id = None
        self._name = None
        self._resources = None
        self._skipped_resources = None
        self.discriminator = None

        self.id = id
        self.name = name
        if resources is not None:
            self.resources = resources
        if skipped_resources is not None:
            self.skipped_resources = skipped_resources

    @property
    def id(self):
        """Gets the id of this CheckpointPlanCreate.

        存储库id

        :return: The id of this CheckpointPlanCreate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckpointPlanCreate.

        存储库id

        :param id: The id of this CheckpointPlanCreate.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CheckpointPlanCreate.

        存储库名称

        :return: The name of this CheckpointPlanCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CheckpointPlanCreate.

        存储库名称

        :param name: The name of this CheckpointPlanCreate.
        :type name: str
        """
        self._name = name

    @property
    def resources(self):
        """Gets the resources of this CheckpointPlanCreate.

        备份对象

        :return: The resources of this CheckpointPlanCreate.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.CheckpointResourceResp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this CheckpointPlanCreate.

        备份对象

        :param resources: The resources of this CheckpointPlanCreate.
        :type resources: list[:class:`huaweicloudsdkcbr.v1.CheckpointResourceResp`]
        """
        self._resources = resources

    @property
    def skipped_resources(self):
        """Gets the skipped_resources of this CheckpointPlanCreate.

        备份时跳过的资源列表

        :return: The skipped_resources of this CheckpointPlanCreate.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.CheckpointCreateSkippedResource`]
        """
        return self._skipped_resources

    @skipped_resources.setter
    def skipped_resources(self, skipped_resources):
        """Sets the skipped_resources of this CheckpointPlanCreate.

        备份时跳过的资源列表

        :param skipped_resources: The skipped_resources of this CheckpointPlanCreate.
        :type skipped_resources: list[:class:`huaweicloudsdkcbr.v1.CheckpointCreateSkippedResource`]
        """
        self._skipped_resources = skipped_resources

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
        if not isinstance(other, CheckpointPlanCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
