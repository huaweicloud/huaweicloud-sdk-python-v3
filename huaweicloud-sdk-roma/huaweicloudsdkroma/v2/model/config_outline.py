# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigOutline:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_id': 'str',
        'config_name': 'str',
        'config_value': 'str',
        'config_time': 'datetime',
        'remark': 'str'
    }

    attribute_map = {
        'config_id': 'config_id',
        'config_name': 'config_name',
        'config_value': 'config_value',
        'config_time': 'config_time',
        'remark': 'remark'
    }

    def __init__(self, config_id=None, config_name=None, config_value=None, config_time=None, remark=None):
        """ConfigOutline

        The model defined in huaweicloud sdk

        :param config_id: 配额编号
        :type config_id: str
        :param config_name: 配额名称
        :type config_name: str
        :param config_value: 配额值  当前实例所在租户该配额对应的数量
        :type config_value: str
        :param config_time: 配额创建时间
        :type config_time: datetime
        :param remark: 配额描述：   - API_NUM_LIMIT：租户可以创建的API个数限制   - APP_NUM_LIMIT：租户可以创建的APP个数限制   - APIGROUP_NUM_LIMIT：租户可以创建的API分组个数限制   - ENVIRONMENT_NUM_LIMIT：租户可以创建的环境个数限制   - VARIABLE_NUM_LIMIT：每个API分组上可以创建的环境变量个数限制   - SIGN_NUM_LIMIT：租户可以创建的签名密钥个数限制   - THROTTLE_NUM_LIMIT：租户可以创建的流控策略个数限制   - APIGROUP_DOMAIN_NUM_LIMIT：每个API分组上可以绑定的自定义域名个数限制   - API_VERSION_NUM_LIMIT：每个API可以保留的发布版本个数限制   - VPC_NUM_LIMIT：租户可以创建的VPC通道个数限制   - VPC_INSTANCE_NUM_LIMIT：每个VPC通道上可以绑定的弹性云服务器个数限制   - API_PARAM_NUM_LIMIT：每个API可以设置的参数个数限制   - API_USER_CALL_LIMIT：每个租户的API单位时间内的请求默认限制   - ACL_NUM_LIMIT：每个租户可以创建的ACL策略个数限制   - APP_THROTTLE_LIMIT：特殊应用流控策略个数限制   - USER_THROTTLE_LIMIT：特殊用户流控策略个数限制   - API_NUM_LIMIT_PER_GROUP：租户每个API分组可以创建的API数量限制   - API_POLICY_NUM_LIMIT：每个API可以设置的策略后端个数限制   - API_CONDITION_NUM_LIMIT：每个API策略后端可以设置的条件个数限制   - SL_DOMAIN_CALL_LIMIT：每个二级域名单位时间内的请求默认限制   - ELB_SWITCH：是否启用ELB通道   - AUTHORIZER_NUM_LIMIT：租户可创建的自定义认证个数限制   - AUTHORIZER_IDENTITY_NUM_LIMIT：每个自定义认证可以设置的身份来源个数限制   - APP_CODE_NUM_LIMIT：每个APP可以创建的APP code数量限制   - REGION_MANAGER_WHITELIST_SERVICES：不校验region manager服务白名单列表，暂不支持   - API_SWAGGER_NUM_LIMIT：单个API分组可以绑定的swagger文档数量限制   - API_TAG_NUM_LIMIT：每个API可以设置的标签个数限制   - LTS_SWITCH：是启用LTS上报   - APP_KEY_SECRET_SWITCH：是否打开APP支持自定义KEY和SECRET的开关，1：开启；2：关闭   - RESPONSE_NUM_LIMIT：分组自定义响应个数限制   - CONFIG_NUM_LIMIT_PER_APP：每个APP可以设置的配置项个数限制   - BACKEND_TOKEN_ALLOW_SWITCH：是否支持普通租户透传后端token，1：开启；2：关闭   - APP_TOKEN_SWITCH：是否启用APPTOKEN   - API_DESIGNER_SWITCH：是否启用api设计器，1：开启；2：关闭   - APP_API_KEY_SWITCH：是否启用APP_API_KEY认证方式   - APP_BASIC_SWITCH：是否启用APP_BASIC认证方式   - APP_JWT_SWITCH：是否启用APP_JWT认证方式   - APP_ROUTE_SWITCH：是否启用APP路由   - PUBLIC_KEY_SWITCH：是否启用PUBLIK_KEY后端认证方式   - APP_SECRET_SWITCH：是否启用APP_SECRET认证方式   - CASCADE_SWITCH：是否启用级联网关   - IS_INIT_API_PATH_HASH：是否执行过API PATH HASH刷新   - APP_QUOTA_NUM_LIMIT：租户可以创建的客户端配额个数   - IS_INIT_API_VERSION：是否执行过API VERSION CANONICAL PATH刷新   - PLUGIN_NUM_LIMIT：租户可以创建的插件个数   - APICLIENT_FIRST_USE_X_HW_ID_SWITCH：ApiClient是否优先使用x-hw-id校验权限   - API_TASK_NUM_LIMIT：[租户可以创建的API定时任务个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - THROTTLE_LOCAL_SWITCH：[是否启用本地流控模式](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - API_TASK_SWITCH：[租户是否支持定时任务](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - SET_HEADERS_NUM_LIMIT_PER_PLUGIN：[租户可以通过插件创建的HTTP头个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - LUA_SCRIPT_SWITCH：[租户是否允许使用lua_script插件](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - LUA_SCRIPT_NUM_LIMIT：[每个实例可以创建的lua_script类型插件个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - SM_DICT_NUM_LIMIT：[每个实例可以创建的数据字典个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - BM_VPC_INSTANCE_GROUP_NUM_LIMIT：[每个实例可以创建的VPC通道后端服务器组个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)
        :type remark: str
        """
        
        

        self._config_id = None
        self._config_name = None
        self._config_value = None
        self._config_time = None
        self._remark = None
        self.discriminator = None

        if config_id is not None:
            self.config_id = config_id
        if config_name is not None:
            self.config_name = config_name
        if config_value is not None:
            self.config_value = config_value
        if config_time is not None:
            self.config_time = config_time
        if remark is not None:
            self.remark = remark

    @property
    def config_id(self):
        """Gets the config_id of this ConfigOutline.

        配额编号

        :return: The config_id of this ConfigOutline.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this ConfigOutline.

        配额编号

        :param config_id: The config_id of this ConfigOutline.
        :type config_id: str
        """
        self._config_id = config_id

    @property
    def config_name(self):
        """Gets the config_name of this ConfigOutline.

        配额名称

        :return: The config_name of this ConfigOutline.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this ConfigOutline.

        配额名称

        :param config_name: The config_name of this ConfigOutline.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def config_value(self):
        """Gets the config_value of this ConfigOutline.

        配额值  当前实例所在租户该配额对应的数量

        :return: The config_value of this ConfigOutline.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        """Sets the config_value of this ConfigOutline.

        配额值  当前实例所在租户该配额对应的数量

        :param config_value: The config_value of this ConfigOutline.
        :type config_value: str
        """
        self._config_value = config_value

    @property
    def config_time(self):
        """Gets the config_time of this ConfigOutline.

        配额创建时间

        :return: The config_time of this ConfigOutline.
        :rtype: datetime
        """
        return self._config_time

    @config_time.setter
    def config_time(self, config_time):
        """Sets the config_time of this ConfigOutline.

        配额创建时间

        :param config_time: The config_time of this ConfigOutline.
        :type config_time: datetime
        """
        self._config_time = config_time

    @property
    def remark(self):
        """Gets the remark of this ConfigOutline.

        配额描述：   - API_NUM_LIMIT：租户可以创建的API个数限制   - APP_NUM_LIMIT：租户可以创建的APP个数限制   - APIGROUP_NUM_LIMIT：租户可以创建的API分组个数限制   - ENVIRONMENT_NUM_LIMIT：租户可以创建的环境个数限制   - VARIABLE_NUM_LIMIT：每个API分组上可以创建的环境变量个数限制   - SIGN_NUM_LIMIT：租户可以创建的签名密钥个数限制   - THROTTLE_NUM_LIMIT：租户可以创建的流控策略个数限制   - APIGROUP_DOMAIN_NUM_LIMIT：每个API分组上可以绑定的自定义域名个数限制   - API_VERSION_NUM_LIMIT：每个API可以保留的发布版本个数限制   - VPC_NUM_LIMIT：租户可以创建的VPC通道个数限制   - VPC_INSTANCE_NUM_LIMIT：每个VPC通道上可以绑定的弹性云服务器个数限制   - API_PARAM_NUM_LIMIT：每个API可以设置的参数个数限制   - API_USER_CALL_LIMIT：每个租户的API单位时间内的请求默认限制   - ACL_NUM_LIMIT：每个租户可以创建的ACL策略个数限制   - APP_THROTTLE_LIMIT：特殊应用流控策略个数限制   - USER_THROTTLE_LIMIT：特殊用户流控策略个数限制   - API_NUM_LIMIT_PER_GROUP：租户每个API分组可以创建的API数量限制   - API_POLICY_NUM_LIMIT：每个API可以设置的策略后端个数限制   - API_CONDITION_NUM_LIMIT：每个API策略后端可以设置的条件个数限制   - SL_DOMAIN_CALL_LIMIT：每个二级域名单位时间内的请求默认限制   - ELB_SWITCH：是否启用ELB通道   - AUTHORIZER_NUM_LIMIT：租户可创建的自定义认证个数限制   - AUTHORIZER_IDENTITY_NUM_LIMIT：每个自定义认证可以设置的身份来源个数限制   - APP_CODE_NUM_LIMIT：每个APP可以创建的APP code数量限制   - REGION_MANAGER_WHITELIST_SERVICES：不校验region manager服务白名单列表，暂不支持   - API_SWAGGER_NUM_LIMIT：单个API分组可以绑定的swagger文档数量限制   - API_TAG_NUM_LIMIT：每个API可以设置的标签个数限制   - LTS_SWITCH：是启用LTS上报   - APP_KEY_SECRET_SWITCH：是否打开APP支持自定义KEY和SECRET的开关，1：开启；2：关闭   - RESPONSE_NUM_LIMIT：分组自定义响应个数限制   - CONFIG_NUM_LIMIT_PER_APP：每个APP可以设置的配置项个数限制   - BACKEND_TOKEN_ALLOW_SWITCH：是否支持普通租户透传后端token，1：开启；2：关闭   - APP_TOKEN_SWITCH：是否启用APPTOKEN   - API_DESIGNER_SWITCH：是否启用api设计器，1：开启；2：关闭   - APP_API_KEY_SWITCH：是否启用APP_API_KEY认证方式   - APP_BASIC_SWITCH：是否启用APP_BASIC认证方式   - APP_JWT_SWITCH：是否启用APP_JWT认证方式   - APP_ROUTE_SWITCH：是否启用APP路由   - PUBLIC_KEY_SWITCH：是否启用PUBLIK_KEY后端认证方式   - APP_SECRET_SWITCH：是否启用APP_SECRET认证方式   - CASCADE_SWITCH：是否启用级联网关   - IS_INIT_API_PATH_HASH：是否执行过API PATH HASH刷新   - APP_QUOTA_NUM_LIMIT：租户可以创建的客户端配额个数   - IS_INIT_API_VERSION：是否执行过API VERSION CANONICAL PATH刷新   - PLUGIN_NUM_LIMIT：租户可以创建的插件个数   - APICLIENT_FIRST_USE_X_HW_ID_SWITCH：ApiClient是否优先使用x-hw-id校验权限   - API_TASK_NUM_LIMIT：[租户可以创建的API定时任务个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - THROTTLE_LOCAL_SWITCH：[是否启用本地流控模式](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - API_TASK_SWITCH：[租户是否支持定时任务](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - SET_HEADERS_NUM_LIMIT_PER_PLUGIN：[租户可以通过插件创建的HTTP头个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - LUA_SCRIPT_SWITCH：[租户是否允许使用lua_script插件](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - LUA_SCRIPT_NUM_LIMIT：[每个实例可以创建的lua_script类型插件个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - SM_DICT_NUM_LIMIT：[每个实例可以创建的数据字典个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - BM_VPC_INSTANCE_GROUP_NUM_LIMIT：[每个实例可以创建的VPC通道后端服务器组个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)

        :return: The remark of this ConfigOutline.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ConfigOutline.

        配额描述：   - API_NUM_LIMIT：租户可以创建的API个数限制   - APP_NUM_LIMIT：租户可以创建的APP个数限制   - APIGROUP_NUM_LIMIT：租户可以创建的API分组个数限制   - ENVIRONMENT_NUM_LIMIT：租户可以创建的环境个数限制   - VARIABLE_NUM_LIMIT：每个API分组上可以创建的环境变量个数限制   - SIGN_NUM_LIMIT：租户可以创建的签名密钥个数限制   - THROTTLE_NUM_LIMIT：租户可以创建的流控策略个数限制   - APIGROUP_DOMAIN_NUM_LIMIT：每个API分组上可以绑定的自定义域名个数限制   - API_VERSION_NUM_LIMIT：每个API可以保留的发布版本个数限制   - VPC_NUM_LIMIT：租户可以创建的VPC通道个数限制   - VPC_INSTANCE_NUM_LIMIT：每个VPC通道上可以绑定的弹性云服务器个数限制   - API_PARAM_NUM_LIMIT：每个API可以设置的参数个数限制   - API_USER_CALL_LIMIT：每个租户的API单位时间内的请求默认限制   - ACL_NUM_LIMIT：每个租户可以创建的ACL策略个数限制   - APP_THROTTLE_LIMIT：特殊应用流控策略个数限制   - USER_THROTTLE_LIMIT：特殊用户流控策略个数限制   - API_NUM_LIMIT_PER_GROUP：租户每个API分组可以创建的API数量限制   - API_POLICY_NUM_LIMIT：每个API可以设置的策略后端个数限制   - API_CONDITION_NUM_LIMIT：每个API策略后端可以设置的条件个数限制   - SL_DOMAIN_CALL_LIMIT：每个二级域名单位时间内的请求默认限制   - ELB_SWITCH：是否启用ELB通道   - AUTHORIZER_NUM_LIMIT：租户可创建的自定义认证个数限制   - AUTHORIZER_IDENTITY_NUM_LIMIT：每个自定义认证可以设置的身份来源个数限制   - APP_CODE_NUM_LIMIT：每个APP可以创建的APP code数量限制   - REGION_MANAGER_WHITELIST_SERVICES：不校验region manager服务白名单列表，暂不支持   - API_SWAGGER_NUM_LIMIT：单个API分组可以绑定的swagger文档数量限制   - API_TAG_NUM_LIMIT：每个API可以设置的标签个数限制   - LTS_SWITCH：是启用LTS上报   - APP_KEY_SECRET_SWITCH：是否打开APP支持自定义KEY和SECRET的开关，1：开启；2：关闭   - RESPONSE_NUM_LIMIT：分组自定义响应个数限制   - CONFIG_NUM_LIMIT_PER_APP：每个APP可以设置的配置项个数限制   - BACKEND_TOKEN_ALLOW_SWITCH：是否支持普通租户透传后端token，1：开启；2：关闭   - APP_TOKEN_SWITCH：是否启用APPTOKEN   - API_DESIGNER_SWITCH：是否启用api设计器，1：开启；2：关闭   - APP_API_KEY_SWITCH：是否启用APP_API_KEY认证方式   - APP_BASIC_SWITCH：是否启用APP_BASIC认证方式   - APP_JWT_SWITCH：是否启用APP_JWT认证方式   - APP_ROUTE_SWITCH：是否启用APP路由   - PUBLIC_KEY_SWITCH：是否启用PUBLIK_KEY后端认证方式   - APP_SECRET_SWITCH：是否启用APP_SECRET认证方式   - CASCADE_SWITCH：是否启用级联网关   - IS_INIT_API_PATH_HASH：是否执行过API PATH HASH刷新   - APP_QUOTA_NUM_LIMIT：租户可以创建的客户端配额个数   - IS_INIT_API_VERSION：是否执行过API VERSION CANONICAL PATH刷新   - PLUGIN_NUM_LIMIT：租户可以创建的插件个数   - APICLIENT_FIRST_USE_X_HW_ID_SWITCH：ApiClient是否优先使用x-hw-id校验权限   - API_TASK_NUM_LIMIT：[租户可以创建的API定时任务个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - THROTTLE_LOCAL_SWITCH：[是否启用本地流控模式](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - API_TASK_SWITCH：[租户是否支持定时任务](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - SET_HEADERS_NUM_LIMIT_PER_PLUGIN：[租户可以通过插件创建的HTTP头个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - LUA_SCRIPT_SWITCH：[租户是否允许使用lua_script插件](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - LUA_SCRIPT_NUM_LIMIT：[每个实例可以创建的lua_script类型插件个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - SM_DICT_NUM_LIMIT：[每个实例可以创建的数据字典个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)   - BM_VPC_INSTANCE_GROUP_NUM_LIMIT：[每个实例可以创建的VPC通道后端服务器组个数限制](tag:hws,hws_hk)[暂未使用](tag:fcs,hcs,hcs_sm,g42,Site)

        :param remark: The remark of this ConfigOutline.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, ConfigOutline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
