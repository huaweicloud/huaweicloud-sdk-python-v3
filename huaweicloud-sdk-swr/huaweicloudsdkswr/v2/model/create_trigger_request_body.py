# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTriggerRequestBody:

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
        'enable': 'str',
        'name': 'str',
        'trigger_mode': 'str',
        'trigger_type': 'str'
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
        'enable': 'enable',
        'name': 'name',
        'trigger_mode': 'trigger_mode',
        'trigger_type': 'trigger_type'
    }

    def __init__(self, action=None, app_type=None, application=None, cluster_id=None, cluster_name=None, cluster_ns=None, condition=None, container=None, enable=None, name=None, trigger_mode=None, trigger_type=None):
        """CreateTriggerRequestBody

        The model defined in huaweicloud sdk

        :param action: 触发动作，update
        :type action: str
        :param app_type: 应用类型，deployments、statefulsets
        :type app_type: str
        :param application: 应用名
        :type application: str
        :param cluster_id: 集群ID（trigger_mode设置为cci时为空)
        :type cluster_id: str
        :param cluster_name: 集群名（trigger_mode设置为cci时为空）
        :type cluster_name: str
        :param cluster_ns: 应用名所在的namespace
        :type cluster_ns: str
        :param condition: 触发条件，type为all时为.*,type为tag时为tag名,type为regular时为正则表达式
        :type condition: str
        :param container: 需更新的container名，默认为所有container
        :type container: str
        :param enable: 是否生效
        :type enable: str
        :param name: 触发器名
        :type name: str
        :param trigger_mode: 触发器类型，cce、cci，默认为cce
        :type trigger_mode: str
        :param trigger_type: 触发条件，all、tag、regular
        :type trigger_type: str
        """
        
        

        self._action = None
        self._app_type = None
        self._application = None
        self._cluster_id = None
        self._cluster_name = None
        self._cluster_ns = None
        self._condition = None
        self._container = None
        self._enable = None
        self._name = None
        self._trigger_mode = None
        self._trigger_type = None
        self.discriminator = None

        self.action = action
        self.app_type = app_type
        self.application = application
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        self.cluster_ns = cluster_ns
        self.condition = condition
        if container is not None:
            self.container = container
        self.enable = enable
        self.name = name
        if trigger_mode is not None:
            self.trigger_mode = trigger_mode
        self.trigger_type = trigger_type

    @property
    def action(self):
        """Gets the action of this CreateTriggerRequestBody.

        触发动作，update

        :return: The action of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateTriggerRequestBody.

        触发动作，update

        :param action: The action of this CreateTriggerRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def app_type(self):
        """Gets the app_type of this CreateTriggerRequestBody.

        应用类型，deployments、statefulsets

        :return: The app_type of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this CreateTriggerRequestBody.

        应用类型，deployments、statefulsets

        :param app_type: The app_type of this CreateTriggerRequestBody.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def application(self):
        """Gets the application of this CreateTriggerRequestBody.

        应用名

        :return: The application of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this CreateTriggerRequestBody.

        应用名

        :param application: The application of this CreateTriggerRequestBody.
        :type application: str
        """
        self._application = application

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateTriggerRequestBody.

        集群ID（trigger_mode设置为cci时为空)

        :return: The cluster_id of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateTriggerRequestBody.

        集群ID（trigger_mode设置为cci时为空)

        :param cluster_id: The cluster_id of this CreateTriggerRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateTriggerRequestBody.

        集群名（trigger_mode设置为cci时为空）

        :return: The cluster_name of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateTriggerRequestBody.

        集群名（trigger_mode设置为cci时为空）

        :param cluster_name: The cluster_name of this CreateTriggerRequestBody.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_ns(self):
        """Gets the cluster_ns of this CreateTriggerRequestBody.

        应用名所在的namespace

        :return: The cluster_ns of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._cluster_ns

    @cluster_ns.setter
    def cluster_ns(self, cluster_ns):
        """Sets the cluster_ns of this CreateTriggerRequestBody.

        应用名所在的namespace

        :param cluster_ns: The cluster_ns of this CreateTriggerRequestBody.
        :type cluster_ns: str
        """
        self._cluster_ns = cluster_ns

    @property
    def condition(self):
        """Gets the condition of this CreateTriggerRequestBody.

        触发条件，type为all时为.*,type为tag时为tag名,type为regular时为正则表达式

        :return: The condition of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this CreateTriggerRequestBody.

        触发条件，type为all时为.*,type为tag时为tag名,type为regular时为正则表达式

        :param condition: The condition of this CreateTriggerRequestBody.
        :type condition: str
        """
        self._condition = condition

    @property
    def container(self):
        """Gets the container of this CreateTriggerRequestBody.

        需更新的container名，默认为所有container

        :return: The container of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this CreateTriggerRequestBody.

        需更新的container名，默认为所有container

        :param container: The container of this CreateTriggerRequestBody.
        :type container: str
        """
        self._container = container

    @property
    def enable(self):
        """Gets the enable of this CreateTriggerRequestBody.

        是否生效

        :return: The enable of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateTriggerRequestBody.

        是否生效

        :param enable: The enable of this CreateTriggerRequestBody.
        :type enable: str
        """
        self._enable = enable

    @property
    def name(self):
        """Gets the name of this CreateTriggerRequestBody.

        触发器名

        :return: The name of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTriggerRequestBody.

        触发器名

        :param name: The name of this CreateTriggerRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def trigger_mode(self):
        """Gets the trigger_mode of this CreateTriggerRequestBody.

        触发器类型，cce、cci，默认为cce

        :return: The trigger_mode of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._trigger_mode

    @trigger_mode.setter
    def trigger_mode(self, trigger_mode):
        """Sets the trigger_mode of this CreateTriggerRequestBody.

        触发器类型，cce、cci，默认为cce

        :param trigger_mode: The trigger_mode of this CreateTriggerRequestBody.
        :type trigger_mode: str
        """
        self._trigger_mode = trigger_mode

    @property
    def trigger_type(self):
        """Gets the trigger_type of this CreateTriggerRequestBody.

        触发条件，all、tag、regular

        :return: The trigger_type of this CreateTriggerRequestBody.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this CreateTriggerRequestBody.

        触发条件，all、tag、regular

        :param trigger_type: The trigger_type of this CreateTriggerRequestBody.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

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
        if not isinstance(other, CreateTriggerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
