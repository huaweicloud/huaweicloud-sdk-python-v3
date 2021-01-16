# coding: utf-8

import pprint
import re

import six





class TriggerHistorys:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'app_type': 'str',
        'application': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'cluster_ns': 'str',
        'condition': 'str',
        'container': 'str',
        'created_at': 'str',
        'creator_name': 'str',
        'detail': 'str',
        'result': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'action': 'action',
        'app_type': 'app_type',
        'application': 'application',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_ns': 'cluster_ns',
        'condition': 'condition',
        'container': 'container',
        'created_at': 'created_at',
        'creator_name': 'creator_name',
        'detail': 'detail',
        'result': 'result',
        'tag': 'tag'
    }

    def __init__(self, action=None, app_type=None, application=None, cluster_id=None, cluster_name=None, cluster_ns=None, condition=None, container=None, created_at=None, creator_name=None, detail=None, result=None, tag=None):
        """TriggerHistorys - a model defined in huaweicloud sdk"""
        
        

        self._action = None
        self._app_type = None
        self._application = None
        self._cluster_id = None
        self._cluster_name = None
        self._cluster_ns = None
        self._condition = None
        self._container = None
        self._created_at = None
        self._creator_name = None
        self._detail = None
        self._result = None
        self._tag = None
        self.discriminator = None

        self.action = action
        self.app_type = app_type
        self.application = application
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_ns = cluster_ns
        self.condition = condition
        self.container = container
        self.created_at = created_at
        self.creator_name = creator_name
        self.detail = detail
        self.result = result
        self.tag = tag

    @property
    def action(self):
        """Gets the action of this TriggerHistorys.

        触发动作，update

        :return: The action of this TriggerHistorys.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this TriggerHistorys.

        触发动作，update

        :param action: The action of this TriggerHistorys.
        :type: str
        """
        self._action = action

    @property
    def app_type(self):
        """Gets the app_type of this TriggerHistorys.

        应用类型，deployments、statefulsets

        :return: The app_type of this TriggerHistorys.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this TriggerHistorys.

        应用类型，deployments、statefulsets

        :param app_type: The app_type of this TriggerHistorys.
        :type: str
        """
        self._app_type = app_type

    @property
    def application(self):
        """Gets the application of this TriggerHistorys.

        应用名

        :return: The application of this TriggerHistorys.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this TriggerHistorys.

        应用名

        :param application: The application of this TriggerHistorys.
        :type: str
        """
        self._application = application

    @property
    def cluster_id(self):
        """Gets the cluster_id of this TriggerHistorys.

        集群ID（cci时为空）

        :return: The cluster_id of this TriggerHistorys.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this TriggerHistorys.

        集群ID（cci时为空）

        :param cluster_id: The cluster_id of this TriggerHistorys.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this TriggerHistorys.

        集群名（cci时为空）

        :return: The cluster_name of this TriggerHistorys.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this TriggerHistorys.

        集群名（cci时为空）

        :param cluster_name: The cluster_name of this TriggerHistorys.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_ns(self):
        """Gets the cluster_ns of this TriggerHistorys.

        应用名所在的namespace

        :return: The cluster_ns of this TriggerHistorys.
        :rtype: str
        """
        return self._cluster_ns

    @cluster_ns.setter
    def cluster_ns(self, cluster_ns):
        """Sets the cluster_ns of this TriggerHistorys.

        应用名所在的namespace

        :param cluster_ns: The cluster_ns of this TriggerHistorys.
        :type: str
        """
        self._cluster_ns = cluster_ns

    @property
    def condition(self):
        """Gets the condition of this TriggerHistorys.

        触发条件，type为all时为.*,type为tag时为tag名,type为regular时为正则表达式

        :return: The condition of this TriggerHistorys.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this TriggerHistorys.

        触发条件，type为all时为.*,type为tag时为tag名,type为regular时为正则表达式

        :param condition: The condition of this TriggerHistorys.
        :type: str
        """
        self._condition = condition

    @property
    def container(self):
        """Gets the container of this TriggerHistorys.

        需更新的container名，默认为所有container

        :return: The container of this TriggerHistorys.
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this TriggerHistorys.

        需更新的container名，默认为所有container

        :param container: The container of this TriggerHistorys.
        :type: str
        """
        self._container = container

    @property
    def created_at(self):
        """Gets the created_at of this TriggerHistorys.

        创建时间

        :return: The created_at of this TriggerHistorys.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TriggerHistorys.

        创建时间

        :param created_at: The created_at of this TriggerHistorys.
        :type: str
        """
        self._created_at = created_at

    @property
    def creator_name(self):
        """Gets the creator_name of this TriggerHistorys.

        创建人

        :return: The creator_name of this TriggerHistorys.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this TriggerHistorys.

        创建人

        :param creator_name: The creator_name of this TriggerHistorys.
        :type: str
        """
        self._creator_name = creator_name

    @property
    def detail(self):
        """Gets the detail of this TriggerHistorys.

        详情

        :return: The detail of this TriggerHistorys.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this TriggerHistorys.

        详情

        :param detail: The detail of this TriggerHistorys.
        :type: str
        """
        self._detail = detail

    @property
    def result(self):
        """Gets the result of this TriggerHistorys.

        更新结果，success、failed

        :return: The result of this TriggerHistorys.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this TriggerHistorys.

        更新结果，success、failed

        :param result: The result of this TriggerHistorys.
        :type: str
        """
        self._result = result

    @property
    def tag(self):
        """Gets the tag of this TriggerHistorys.

        触发的版本号

        :return: The tag of this TriggerHistorys.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this TriggerHistorys.

        触发的版本号

        :param tag: The tag of this TriggerHistorys.
        :type: str
        """
        self._tag = tag

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TriggerHistorys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
