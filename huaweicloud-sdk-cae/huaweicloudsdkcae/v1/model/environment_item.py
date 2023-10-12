# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentItem:

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
        'job_id': 'str',
        'status': 'str',
        'annotations': 'dict(str, str)',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'job_id': 'job_id',
        'status': 'status',
        'annotations': 'annotations',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, job_id=None, status=None, annotations=None, created_at=None, updated_at=None):
        """EnvironmentItem

        The model defined in huaweicloud sdk

        :param id: 环境ID。
        :type id: str
        :param name: 环境名称。
        :type name: str
        :param job_id: 任务ID。
        :type job_id: str
        :param status: 环境状态。
        :type status: str
        :param annotations: 环境附加属性。 - cluster_id：CCE集群ID。 - enterprise_project_id：企业项目ID。 - group_name：主环境绑定的SWR组织名称。 - inbound_eip_addr：负载均衡绑定EIP地址。 - namespace：CCE集群命名空间。 - public_elb_id：ELB ID，主环境绑定的负载均衡ID。 - type：环境类型，当前仅支持exclusive类型。 - vpc_id：主环境绑定的VPC ID。
        :type annotations: dict(str, str)
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._job_id = None
        self._status = None
        self._annotations = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if annotations is not None:
            self.annotations = annotations
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this EnvironmentItem.

        环境ID。

        :return: The id of this EnvironmentItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnvironmentItem.

        环境ID。

        :param id: The id of this EnvironmentItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EnvironmentItem.

        环境名称。

        :return: The name of this EnvironmentItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentItem.

        环境名称。

        :param name: The name of this EnvironmentItem.
        :type name: str
        """
        self._name = name

    @property
    def job_id(self):
        """Gets the job_id of this EnvironmentItem.

        任务ID。

        :return: The job_id of this EnvironmentItem.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this EnvironmentItem.

        任务ID。

        :param job_id: The job_id of this EnvironmentItem.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this EnvironmentItem.

        环境状态。

        :return: The status of this EnvironmentItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EnvironmentItem.

        环境状态。

        :param status: The status of this EnvironmentItem.
        :type status: str
        """
        self._status = status

    @property
    def annotations(self):
        """Gets the annotations of this EnvironmentItem.

        环境附加属性。 - cluster_id：CCE集群ID。 - enterprise_project_id：企业项目ID。 - group_name：主环境绑定的SWR组织名称。 - inbound_eip_addr：负载均衡绑定EIP地址。 - namespace：CCE集群命名空间。 - public_elb_id：ELB ID，主环境绑定的负载均衡ID。 - type：环境类型，当前仅支持exclusive类型。 - vpc_id：主环境绑定的VPC ID。

        :return: The annotations of this EnvironmentItem.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this EnvironmentItem.

        环境附加属性。 - cluster_id：CCE集群ID。 - enterprise_project_id：企业项目ID。 - group_name：主环境绑定的SWR组织名称。 - inbound_eip_addr：负载均衡绑定EIP地址。 - namespace：CCE集群命名空间。 - public_elb_id：ELB ID，主环境绑定的负载均衡ID。 - type：环境类型，当前仅支持exclusive类型。 - vpc_id：主环境绑定的VPC ID。

        :param annotations: The annotations of this EnvironmentItem.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def created_at(self):
        """Gets the created_at of this EnvironmentItem.

        创建时间。

        :return: The created_at of this EnvironmentItem.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EnvironmentItem.

        创建时间。

        :param created_at: The created_at of this EnvironmentItem.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EnvironmentItem.

        更新时间。

        :return: The updated_at of this EnvironmentItem.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EnvironmentItem.

        更新时间。

        :param updated_at: The updated_at of this EnvironmentItem.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, EnvironmentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
