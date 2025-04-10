# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'status': 'str',
        'type': 'str',
        'solution': 'str',
        'hotfix_versions': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'status': 'status',
        'type': 'type',
        'solution': 'solution',
        'hotfix_versions': 'hotfix_versions'
    }

    def __init__(self, instance_id=None, instance_name=None, status=None, type=None, solution=None, hotfix_versions=None):
        r"""InstanceDetail

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param status: 实例状态。
        :type status: str
        :param type: 实例类型。
        :type type: str
        :param solution: 实例部署形态。
        :type solution: str
        :param hotfix_versions: 已升级热补丁版本。
        :type hotfix_versions: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._status = None
        self._type = None
        self._solution = None
        self._hotfix_versions = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if solution is not None:
            self.solution = solution
        if hotfix_versions is not None:
            self.hotfix_versions = hotfix_versions

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceDetail.

        实例ID。

        :return: The instance_id of this InstanceDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceDetail.

        实例ID。

        :param instance_id: The instance_id of this InstanceDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this InstanceDetail.

        实例名称。

        :return: The instance_name of this InstanceDetail.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this InstanceDetail.

        实例名称。

        :param instance_name: The instance_name of this InstanceDetail.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def status(self):
        r"""Gets the status of this InstanceDetail.

        实例状态。

        :return: The status of this InstanceDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceDetail.

        实例状态。

        :param status: The status of this InstanceDetail.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this InstanceDetail.

        实例类型。

        :return: The type of this InstanceDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this InstanceDetail.

        实例类型。

        :param type: The type of this InstanceDetail.
        :type type: str
        """
        self._type = type

    @property
    def solution(self):
        r"""Gets the solution of this InstanceDetail.

        实例部署形态。

        :return: The solution of this InstanceDetail.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this InstanceDetail.

        实例部署形态。

        :param solution: The solution of this InstanceDetail.
        :type solution: str
        """
        self._solution = solution

    @property
    def hotfix_versions(self):
        r"""Gets the hotfix_versions of this InstanceDetail.

        已升级热补丁版本。

        :return: The hotfix_versions of this InstanceDetail.
        :rtype: str
        """
        return self._hotfix_versions

    @hotfix_versions.setter
    def hotfix_versions(self, hotfix_versions):
        r"""Sets the hotfix_versions of this InstanceDetail.

        已升级热补丁版本。

        :param hotfix_versions: The hotfix_versions of this InstanceDetail.
        :type hotfix_versions: str
        """
        self._hotfix_versions = hotfix_versions

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
        if not isinstance(other, InstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
