# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLtsLogPolicyRespondBodyInstance:

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
        'mode': 'str',
        'datastore': 'ListLtsLogPolicyRespondBodyInstanceDatastore',
        'status': 'str',
        'enterprise_project_id': 'str',
        'actions': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'mode': 'mode',
        'datastore': 'datastore',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'actions': 'actions'
    }

    def __init__(self, id=None, name=None, mode=None, datastore=None, status=None, enterprise_project_id=None, actions=None):
        """ListLtsLogPolicyRespondBodyInstance

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名字。
        :type name: str
        :param mode: 实例类型，对应单节点，副本集，集群三种。
        :type mode: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdds.v3.ListLtsLogPolicyRespondBodyInstanceDatastore`
        :param status: 实例状态。
        :type status: str
        :param enterprise_project_id: 实例归属的企业项目ID，如果是default企业项目，值为0，如果是其他企业项目，请参考企业项目相关内容。
        :type enterprise_project_id: str
        :param actions: 实例所有正在执行的动作。
        :type actions: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._mode = None
        self._datastore = None
        self._status = None
        self._enterprise_project_id = None
        self._actions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if datastore is not None:
            self.datastore = datastore
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if actions is not None:
            self.actions = actions

    @property
    def id(self):
        """Gets the id of this ListLtsLogPolicyRespondBodyInstance.

        实例ID。

        :return: The id of this ListLtsLogPolicyRespondBodyInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListLtsLogPolicyRespondBodyInstance.

        实例ID。

        :param id: The id of this ListLtsLogPolicyRespondBodyInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListLtsLogPolicyRespondBodyInstance.

        实例名字。

        :return: The name of this ListLtsLogPolicyRespondBodyInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListLtsLogPolicyRespondBodyInstance.

        实例名字。

        :param name: The name of this ListLtsLogPolicyRespondBodyInstance.
        :type name: str
        """
        self._name = name

    @property
    def mode(self):
        """Gets the mode of this ListLtsLogPolicyRespondBodyInstance.

        实例类型，对应单节点，副本集，集群三种。

        :return: The mode of this ListLtsLogPolicyRespondBodyInstance.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ListLtsLogPolicyRespondBodyInstance.

        实例类型，对应单节点，副本集，集群三种。

        :param mode: The mode of this ListLtsLogPolicyRespondBodyInstance.
        :type mode: str
        """
        self._mode = mode

    @property
    def datastore(self):
        """Gets the datastore of this ListLtsLogPolicyRespondBodyInstance.

        :return: The datastore of this ListLtsLogPolicyRespondBodyInstance.
        :rtype: :class:`huaweicloudsdkdds.v3.ListLtsLogPolicyRespondBodyInstanceDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ListLtsLogPolicyRespondBodyInstance.

        :param datastore: The datastore of this ListLtsLogPolicyRespondBodyInstance.
        :type datastore: :class:`huaweicloudsdkdds.v3.ListLtsLogPolicyRespondBodyInstanceDatastore`
        """
        self._datastore = datastore

    @property
    def status(self):
        """Gets the status of this ListLtsLogPolicyRespondBodyInstance.

        实例状态。

        :return: The status of this ListLtsLogPolicyRespondBodyInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListLtsLogPolicyRespondBodyInstance.

        实例状态。

        :param status: The status of this ListLtsLogPolicyRespondBodyInstance.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListLtsLogPolicyRespondBodyInstance.

        实例归属的企业项目ID，如果是default企业项目，值为0，如果是其他企业项目，请参考企业项目相关内容。

        :return: The enterprise_project_id of this ListLtsLogPolicyRespondBodyInstance.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListLtsLogPolicyRespondBodyInstance.

        实例归属的企业项目ID，如果是default企业项目，值为0，如果是其他企业项目，请参考企业项目相关内容。

        :param enterprise_project_id: The enterprise_project_id of this ListLtsLogPolicyRespondBodyInstance.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def actions(self):
        """Gets the actions of this ListLtsLogPolicyRespondBodyInstance.

        实例所有正在执行的动作。

        :return: The actions of this ListLtsLogPolicyRespondBodyInstance.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ListLtsLogPolicyRespondBodyInstance.

        实例所有正在执行的动作。

        :param actions: The actions of this ListLtsLogPolicyRespondBodyInstance.
        :type actions: list[str]
        """
        self._actions = actions

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
        if not isinstance(other, ListLtsLogPolicyRespondBodyInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
