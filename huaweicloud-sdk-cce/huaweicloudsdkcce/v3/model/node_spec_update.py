# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSpecUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'taints': 'list[Taint]',
        'k8s_tags': 'dict(str, str)',
        'user_tags': 'list[UserTag]',
        'initialized_conditions': 'list[str]'
    }

    attribute_map = {
        'taints': 'taints',
        'k8s_tags': 'k8sTags',
        'user_tags': 'userTags',
        'initialized_conditions': 'initializedConditions'
    }

    def __init__(self, taints=None, k8s_tags=None, user_tags=None, initialized_conditions=None):
        """NodeSpecUpdate

        The model defined in huaweicloud sdk

        :param taints: 支持给创建出来的节点加Taints来设置反亲和性，taints配置不超过20条。默认值为空。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  &#x60;&#x60;&#x60; \&quot;taints\&quot;: [{   \&quot;key\&quot;: \&quot;status\&quot;,   \&quot;value\&quot;: \&quot;unavailable\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }, {   \&quot;key\&quot;: \&quot;looks\&quot;,   \&quot;value\&quot;: \&quot;bad\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }] &#x60;&#x60;&#x60; 
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        :param k8s_tags: 格式为key/value键值对。键值对个数不超过20条。默认值为空。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。  示例： &#x60;&#x60;&#x60; \&quot;k8sTags\&quot;: {   \&quot;key\&quot;: \&quot;value\&quot; } &#x60;&#x60;&#x60; 
        :type k8s_tags: dict(str, str)
        :param user_tags: 云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。默认值为空。
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        :param initialized_conditions: 自定义初始化标记。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。  cce支持自定义初始化标记，在接收到initializedConditions参数后，会将参数值转换成节点标签，随节点下发，例如：cloudprovider.openvessel.io/inject-initialized-conditions&#x3D;CCEInitial_CustomedInitial。  当节点上设置了此标签，会轮询节点的status.Conditions，查看conditions的type是否存在标记名，如CCEInitial、CustomedInitial标记，如果存在所有传入的标记，且状态为True，认为节点初始化完成，则移除初始化污点。  默认值为空。  - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个 
        :type initialized_conditions: list[str]
        """
        
        

        self._taints = None
        self._k8s_tags = None
        self._user_tags = None
        self._initialized_conditions = None
        self.discriminator = None

        self.taints = taints
        self.k8s_tags = k8s_tags
        self.user_tags = user_tags
        if initialized_conditions is not None:
            self.initialized_conditions = initialized_conditions

    @property
    def taints(self):
        """Gets the taints of this NodeSpecUpdate.

        支持给创建出来的节点加Taints来设置反亲和性，taints配置不超过20条。默认值为空。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ``` 

        :return: The taints of this NodeSpecUpdate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        """Sets the taints of this NodeSpecUpdate.

        支持给创建出来的节点加Taints来设置反亲和性，taints配置不超过20条。默认值为空。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ``` 

        :param taints: The taints of this NodeSpecUpdate.
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        self._taints = taints

    @property
    def k8s_tags(self):
        """Gets the k8s_tags of this NodeSpecUpdate.

        格式为key/value键值对。键值对个数不超过20条。默认值为空。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。  示例： ``` \"k8sTags\": {   \"key\": \"value\" } ``` 

        :return: The k8s_tags of this NodeSpecUpdate.
        :rtype: dict(str, str)
        """
        return self._k8s_tags

    @k8s_tags.setter
    def k8s_tags(self, k8s_tags):
        """Sets the k8s_tags of this NodeSpecUpdate.

        格式为key/value键值对。键值对个数不超过20条。默认值为空。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。  示例： ``` \"k8sTags\": {   \"key\": \"value\" } ``` 

        :param k8s_tags: The k8s_tags of this NodeSpecUpdate.
        :type k8s_tags: dict(str, str)
        """
        self._k8s_tags = k8s_tags

    @property
    def user_tags(self):
        """Gets the user_tags of this NodeSpecUpdate.

        云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。默认值为空。

        :return: The user_tags of this NodeSpecUpdate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        return self._user_tags

    @user_tags.setter
    def user_tags(self, user_tags):
        """Sets the user_tags of this NodeSpecUpdate.

        云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为8个。默认值为空。

        :param user_tags: The user_tags of this NodeSpecUpdate.
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        self._user_tags = user_tags

    @property
    def initialized_conditions(self):
        """Gets the initialized_conditions of this NodeSpecUpdate.

        自定义初始化标记。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。  cce支持自定义初始化标记，在接收到initializedConditions参数后，会将参数值转换成节点标签，随节点下发，例如：cloudprovider.openvessel.io/inject-initialized-conditions=CCEInitial_CustomedInitial。  当节点上设置了此标签，会轮询节点的status.Conditions，查看conditions的type是否存在标记名，如CCEInitial、CustomedInitial标记，如果存在所有传入的标记，且状态为True，认为节点初始化完成，则移除初始化污点。  默认值为空。  - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个 

        :return: The initialized_conditions of this NodeSpecUpdate.
        :rtype: list[str]
        """
        return self._initialized_conditions

    @initialized_conditions.setter
    def initialized_conditions(self, initialized_conditions):
        """Sets the initialized_conditions of this NodeSpecUpdate.

        自定义初始化标记。  CCE节点在初始化完成之前，会打上初始化未完成污点（node.cloudprovider.kubernetes.io/uninitialized）防止pod调度到节点上。  cce支持自定义初始化标记，在接收到initializedConditions参数后，会将参数值转换成节点标签，随节点下发，例如：cloudprovider.openvessel.io/inject-initialized-conditions=CCEInitial_CustomedInitial。  当节点上设置了此标签，会轮询节点的status.Conditions，查看conditions的type是否存在标记名，如CCEInitial、CustomedInitial标记，如果存在所有传入的标记，且状态为True，认为节点初始化完成，则移除初始化污点。  默认值为空。  - 必须以字母、数字组成，长度范围1-20位。 - 标记数量不超过2个 

        :param initialized_conditions: The initialized_conditions of this NodeSpecUpdate.
        :type initialized_conditions: list[str]
        """
        self._initialized_conditions = initialized_conditions

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
        if not isinstance(other, NodeSpecUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
