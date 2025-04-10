# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBatchTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'task_name': 'str',
        'task_type': 'str',
        'task_mode': 'str',
        'task_ext_info': 'object',
        'targets': 'list[str]',
        'targets_filter': 'dict(str, object)',
        'document': 'object',
        'task_policy': 'TaskPolicy',
        'document_source': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'task_mode': 'task_mode',
        'task_ext_info': 'task_ext_info',
        'targets': 'targets',
        'targets_filter': 'targets_filter',
        'document': 'document',
        'task_policy': 'task_policy',
        'document_source': 'document_source'
    }

    def __init__(self, app_id=None, task_name=None, task_type=None, task_mode=None, task_ext_info=None, targets=None, targets_filter=None, document=None, task_policy=None, document_source=None):
        r"""CreateBatchTask

        The model defined in huaweicloud sdk

        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的批量任务归属到哪个资源空间下，否则创建的批量任务将会归属到[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param task_name: **参数说明**：批量任务名称。 **取值范围**：长度不超过128，只允许中文、字母、数字、下划线（_）的组合。
        :type task_name: str
        :param task_type: **参数说明**：批量任务类型。 **取值范围**： - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 - createDevices: 批量创建设备任务 - deleteDevices: 批量删除设备任务 - freezeDevices: 批量冻结设备任务 - unfreezeDevices: 批量解冻设备任务 - createCommands: 批量创建同步命令任务 - createAsyncCommands: 批量创建异步命令任务 - createMessages: 批量创建消息任务 - updateDeviceShadows：批量配置设备影子任务 - updateDevices：批量更新设备任务
        :type task_type: str
        :param task_mode: **参数说明**：批量任务的模式，当前只支持网关模式，当task_type为firmwareUpgrade，softwareUpgrade支持该参数。软固件升级的场景下，若升级的设备为某个网关的子设备，则平台下发获取版本信息通知和平台下发升级通知将携带task_id（软固件升级批量任务的任务ID）和sub_device_count（批量任务中网关设备包含的升级子设备数量）字段。 **取值范围**：GATEWAY: 网关模式。
        :type task_mode: str
        :param task_ext_info: **参数说明**：批量任务额外扩展信息，当task_type为firmwareUpgrade，softwareUpgrade支持该参数。软固件升级的场景下，平台下发获取版本信息通知和平台下发升级通知将携带该字段。 **取值范围**：最长不超过512个字符。
        :type task_ext_info: object
        :param targets: **参数说明**：执行批量任务的目标，此处填写device_id列表，且最多支持3万个device_id。当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，支持该参数。同时使用targets、targets_filter、document_source参数时，只有一个参数会生效，且平台优先使用targets，其次是targets_filter，最后是document_source。 **取值范围**：device_id列表。device_id支持长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type targets: list[str]
        :param targets_filter: **参数说明**：任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\&quot;e495cf17-ff79-4294-8f64-4d367919d665\&quot;]，任务则会筛选出来符合该群组条件的设备作为目标）。当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，支持该参数。同时使用targets、targets_filter、document_source参数时，只有一个参数会生效，且平台优先使用targets，其次是targets_filter，最后是document_source。
        :type targets_filter: dict(str, object)
        :param document: **参数说明**：执行任务数据文档，Json格式，Json里面是(K,V)键值对。当task_type为firmwareUpgrade，softwareUpgrade，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，支持该参数。 - softwareUpgrade|firmwareUpgrade，需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得。eg：“{\&quot;package_id\&quot;: \&quot;32822e5744a45ede319d2c50\&quot;}”。 - createCommands，需要填写同步命令相关参数，eg：“{\&quot;service_id\&quot;:\&quot;water\&quot;,\&quot;command_name\&quot;:\&quot;ON_OFF\&quot;,\&quot;paras\&quot;:{\&quot;value\&quot;:\&quot;ON\&quot;}}”，参考[[设备同步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0038.html)](tag:hws)[[设备同步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0038.html)](tag:hws_hk))。 - createAsyncCommands，需要填写异步命令相关参数，eg：“{\&quot;service_id\&quot;:\&quot;water\&quot;,\&quot;command_name\&quot;:\&quot;ON_OFF\&quot;,\&quot;paras\&quot;:{\&quot;value\&quot;:\&quot;ON\&quot;},\&quot;expire_time\&quot;:0,\&quot;send_strategy\&quot;:\&quot;immediately\&quot;}”，参考[[设备异步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0040.html)](tag:hws)[[设备异步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0040.html)](tag:hws_hk))。 - createMessages，需要填写消息下发相关参数，eg：“{\&quot;message_id\&quot;:\&quot;99b32da9-cd17-4cdf-a286-f6e849cbc364\&quot;,\&quot;name\&quot;:\&quot;messageName\&quot;,\&quot;message\&quot;:\&quot;HelloWorld\&quot;,\&quot;encoding\&quot;:\&quot;none\&quot;,\&quot;payload_format\&quot;:\&quot;standard\&quot;,\&quot;topic\&quot;:\&quot;messageDown\&quot;,\&quot;topic_full_name\&quot;:\&quot;/device/message/down\&quot;}”，参考[[下发设备消息](https://support.huaweicloud.com/api-iothub/iot_06_v5_0059.html)](tag:hws)[[下发设备消息](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0059.html)](tag:hws_hk))。 - updateDeviceShadows，需要填写配置设备影子相关参数，eg：“{\&quot;shadow\&quot;: [{\&quot;service_id\&quot;: \&quot;WaterMeter\&quot;,\&quot;desired\&quot;: {\&quot;temperature\&quot;: \&quot;60\&quot;}}]}”，参考[[配置设备影子预期数据](https://support.huaweicloud.com/api-iothub/iot_06_v5_0072.html)](tag:hws)[[配置设备影子预期数据](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0072.html)](tag:hws_hk))。限制说明：1. service_id和desired参数必填。2. 配置的service_id数量不大于5个且service_id不能重复。3. 配置参数内容大小不超过10K。
        :type document: object
        :param task_policy: 
        :type task_policy: :class:`huaweicloudsdkiotda.v5.TaskPolicy`
        :param document_source: **参数说明**：上传的批量任务文件ID。当task_type为createDevices，updateDevices，deleteDevices，freezeDevices，unfreezeDevices时，支持该参数。使用该参数时，需要先调用批量任务的文件管理接口上传文件来获取文件ID，文件样例请参见 [批量注册设备模板](https://iot-developer.obs.cn-north-4.myhuaweicloud.com/IoTM/2023-3/BatchCreateDevices_Template.xlsx)，[批量更新设备模板](https://iot-developer.obs.cn-north-4.myhuaweicloud.com/IoTM/2023-3/BatchUpdateDevices_Template.xlsx)，[批量删除设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchDeleteDevices_Template.xlsx)，[批量冻结设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchFreezeDevices_Template.xlsx)，[批量解冻设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchUnfreezeDevices_Template.xlsx)。同时使用targets、targets_filter、document_source参数时，只有一个参数会生效，且平台优先使用targets，其次是targets_filter，最后是document_source。
        :type document_source: str
        """
        
        

        self._app_id = None
        self._task_name = None
        self._task_type = None
        self._task_mode = None
        self._task_ext_info = None
        self._targets = None
        self._targets_filter = None
        self._document = None
        self._task_policy = None
        self._document_source = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        self.task_name = task_name
        self.task_type = task_type
        if task_mode is not None:
            self.task_mode = task_mode
        if task_ext_info is not None:
            self.task_ext_info = task_ext_info
        if targets is not None:
            self.targets = targets
        if targets_filter is not None:
            self.targets_filter = targets_filter
        if document is not None:
            self.document = document
        if task_policy is not None:
            self.task_policy = task_policy
        if document_source is not None:
            self.document_source = document_source

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateBatchTask.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的批量任务归属到哪个资源空间下，否则创建的批量任务将会归属到[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this CreateBatchTask.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateBatchTask.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的批量任务归属到哪个资源空间下，否则创建的批量任务将会归属到[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this CreateBatchTask.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def task_name(self):
        r"""Gets the task_name of this CreateBatchTask.

        **参数说明**：批量任务名称。 **取值范围**：长度不超过128，只允许中文、字母、数字、下划线（_）的组合。

        :return: The task_name of this CreateBatchTask.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CreateBatchTask.

        **参数说明**：批量任务名称。 **取值范围**：长度不超过128，只允许中文、字母、数字、下划线（_）的组合。

        :param task_name: The task_name of this CreateBatchTask.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        r"""Gets the task_type of this CreateBatchTask.

        **参数说明**：批量任务类型。 **取值范围**： - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 - createDevices: 批量创建设备任务 - deleteDevices: 批量删除设备任务 - freezeDevices: 批量冻结设备任务 - unfreezeDevices: 批量解冻设备任务 - createCommands: 批量创建同步命令任务 - createAsyncCommands: 批量创建异步命令任务 - createMessages: 批量创建消息任务 - updateDeviceShadows：批量配置设备影子任务 - updateDevices：批量更新设备任务

        :return: The task_type of this CreateBatchTask.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this CreateBatchTask.

        **参数说明**：批量任务类型。 **取值范围**： - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 - createDevices: 批量创建设备任务 - deleteDevices: 批量删除设备任务 - freezeDevices: 批量冻结设备任务 - unfreezeDevices: 批量解冻设备任务 - createCommands: 批量创建同步命令任务 - createAsyncCommands: 批量创建异步命令任务 - createMessages: 批量创建消息任务 - updateDeviceShadows：批量配置设备影子任务 - updateDevices：批量更新设备任务

        :param task_type: The task_type of this CreateBatchTask.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def task_mode(self):
        r"""Gets the task_mode of this CreateBatchTask.

        **参数说明**：批量任务的模式，当前只支持网关模式，当task_type为firmwareUpgrade，softwareUpgrade支持该参数。软固件升级的场景下，若升级的设备为某个网关的子设备，则平台下发获取版本信息通知和平台下发升级通知将携带task_id（软固件升级批量任务的任务ID）和sub_device_count（批量任务中网关设备包含的升级子设备数量）字段。 **取值范围**：GATEWAY: 网关模式。

        :return: The task_mode of this CreateBatchTask.
        :rtype: str
        """
        return self._task_mode

    @task_mode.setter
    def task_mode(self, task_mode):
        r"""Sets the task_mode of this CreateBatchTask.

        **参数说明**：批量任务的模式，当前只支持网关模式，当task_type为firmwareUpgrade，softwareUpgrade支持该参数。软固件升级的场景下，若升级的设备为某个网关的子设备，则平台下发获取版本信息通知和平台下发升级通知将携带task_id（软固件升级批量任务的任务ID）和sub_device_count（批量任务中网关设备包含的升级子设备数量）字段。 **取值范围**：GATEWAY: 网关模式。

        :param task_mode: The task_mode of this CreateBatchTask.
        :type task_mode: str
        """
        self._task_mode = task_mode

    @property
    def task_ext_info(self):
        r"""Gets the task_ext_info of this CreateBatchTask.

        **参数说明**：批量任务额外扩展信息，当task_type为firmwareUpgrade，softwareUpgrade支持该参数。软固件升级的场景下，平台下发获取版本信息通知和平台下发升级通知将携带该字段。 **取值范围**：最长不超过512个字符。

        :return: The task_ext_info of this CreateBatchTask.
        :rtype: object
        """
        return self._task_ext_info

    @task_ext_info.setter
    def task_ext_info(self, task_ext_info):
        r"""Sets the task_ext_info of this CreateBatchTask.

        **参数说明**：批量任务额外扩展信息，当task_type为firmwareUpgrade，softwareUpgrade支持该参数。软固件升级的场景下，平台下发获取版本信息通知和平台下发升级通知将携带该字段。 **取值范围**：最长不超过512个字符。

        :param task_ext_info: The task_ext_info of this CreateBatchTask.
        :type task_ext_info: object
        """
        self._task_ext_info = task_ext_info

    @property
    def targets(self):
        r"""Gets the targets of this CreateBatchTask.

        **参数说明**：执行批量任务的目标，此处填写device_id列表，且最多支持3万个device_id。当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，支持该参数。同时使用targets、targets_filter、document_source参数时，只有一个参数会生效，且平台优先使用targets，其次是targets_filter，最后是document_source。 **取值范围**：device_id列表。device_id支持长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The targets of this CreateBatchTask.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this CreateBatchTask.

        **参数说明**：执行批量任务的目标，此处填写device_id列表，且最多支持3万个device_id。当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，支持该参数。同时使用targets、targets_filter、document_source参数时，只有一个参数会生效，且平台优先使用targets，其次是targets_filter，最后是document_source。 **取值范围**：device_id列表。device_id支持长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param targets: The targets of this CreateBatchTask.
        :type targets: list[str]
        """
        self._targets = targets

    @property
    def targets_filter(self):
        r"""Gets the targets_filter of this CreateBatchTask.

        **参数说明**：任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\"e495cf17-ff79-4294-8f64-4d367919d665\"]，任务则会筛选出来符合该群组条件的设备作为目标）。当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，支持该参数。同时使用targets、targets_filter、document_source参数时，只有一个参数会生效，且平台优先使用targets，其次是targets_filter，最后是document_source。

        :return: The targets_filter of this CreateBatchTask.
        :rtype: dict(str, object)
        """
        return self._targets_filter

    @targets_filter.setter
    def targets_filter(self, targets_filter):
        r"""Sets the targets_filter of this CreateBatchTask.

        **参数说明**：任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\"e495cf17-ff79-4294-8f64-4d367919d665\"]，任务则会筛选出来符合该群组条件的设备作为目标）。当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，支持该参数。同时使用targets、targets_filter、document_source参数时，只有一个参数会生效，且平台优先使用targets，其次是targets_filter，最后是document_source。

        :param targets_filter: The targets_filter of this CreateBatchTask.
        :type targets_filter: dict(str, object)
        """
        self._targets_filter = targets_filter

    @property
    def document(self):
        r"""Gets the document of this CreateBatchTask.

        **参数说明**：执行任务数据文档，Json格式，Json里面是(K,V)键值对。当task_type为firmwareUpgrade，softwareUpgrade，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，支持该参数。 - softwareUpgrade|firmwareUpgrade，需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得。eg：“{\"package_id\": \"32822e5744a45ede319d2c50\"}”。 - createCommands，需要填写同步命令相关参数，eg：“{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"}}”，参考[[设备同步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0038.html)](tag:hws)[[设备同步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0038.html)](tag:hws_hk))。 - createAsyncCommands，需要填写异步命令相关参数，eg：“{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"},\"expire_time\":0,\"send_strategy\":\"immediately\"}”，参考[[设备异步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0040.html)](tag:hws)[[设备异步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0040.html)](tag:hws_hk))。 - createMessages，需要填写消息下发相关参数，eg：“{\"message_id\":\"99b32da9-cd17-4cdf-a286-f6e849cbc364\",\"name\":\"messageName\",\"message\":\"HelloWorld\",\"encoding\":\"none\",\"payload_format\":\"standard\",\"topic\":\"messageDown\",\"topic_full_name\":\"/device/message/down\"}”，参考[[下发设备消息](https://support.huaweicloud.com/api-iothub/iot_06_v5_0059.html)](tag:hws)[[下发设备消息](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0059.html)](tag:hws_hk))。 - updateDeviceShadows，需要填写配置设备影子相关参数，eg：“{\"shadow\": [{\"service_id\": \"WaterMeter\",\"desired\": {\"temperature\": \"60\"}}]}”，参考[[配置设备影子预期数据](https://support.huaweicloud.com/api-iothub/iot_06_v5_0072.html)](tag:hws)[[配置设备影子预期数据](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0072.html)](tag:hws_hk))。限制说明：1. service_id和desired参数必填。2. 配置的service_id数量不大于5个且service_id不能重复。3. 配置参数内容大小不超过10K。

        :return: The document of this CreateBatchTask.
        :rtype: object
        """
        return self._document

    @document.setter
    def document(self, document):
        r"""Sets the document of this CreateBatchTask.

        **参数说明**：执行任务数据文档，Json格式，Json里面是(K,V)键值对。当task_type为firmwareUpgrade，softwareUpgrade，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，支持该参数。 - softwareUpgrade|firmwareUpgrade，需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得。eg：“{\"package_id\": \"32822e5744a45ede319d2c50\"}”。 - createCommands，需要填写同步命令相关参数，eg：“{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"}}”，参考[[设备同步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0038.html)](tag:hws)[[设备同步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0038.html)](tag:hws_hk))。 - createAsyncCommands，需要填写异步命令相关参数，eg：“{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"},\"expire_time\":0,\"send_strategy\":\"immediately\"}”，参考[[设备异步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0040.html)](tag:hws)[[设备异步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0040.html)](tag:hws_hk))。 - createMessages，需要填写消息下发相关参数，eg：“{\"message_id\":\"99b32da9-cd17-4cdf-a286-f6e849cbc364\",\"name\":\"messageName\",\"message\":\"HelloWorld\",\"encoding\":\"none\",\"payload_format\":\"standard\",\"topic\":\"messageDown\",\"topic_full_name\":\"/device/message/down\"}”，参考[[下发设备消息](https://support.huaweicloud.com/api-iothub/iot_06_v5_0059.html)](tag:hws)[[下发设备消息](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0059.html)](tag:hws_hk))。 - updateDeviceShadows，需要填写配置设备影子相关参数，eg：“{\"shadow\": [{\"service_id\": \"WaterMeter\",\"desired\": {\"temperature\": \"60\"}}]}”，参考[[配置设备影子预期数据](https://support.huaweicloud.com/api-iothub/iot_06_v5_0072.html)](tag:hws)[[配置设备影子预期数据](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0072.html)](tag:hws_hk))。限制说明：1. service_id和desired参数必填。2. 配置的service_id数量不大于5个且service_id不能重复。3. 配置参数内容大小不超过10K。

        :param document: The document of this CreateBatchTask.
        :type document: object
        """
        self._document = document

    @property
    def task_policy(self):
        r"""Gets the task_policy of this CreateBatchTask.

        :return: The task_policy of this CreateBatchTask.
        :rtype: :class:`huaweicloudsdkiotda.v5.TaskPolicy`
        """
        return self._task_policy

    @task_policy.setter
    def task_policy(self, task_policy):
        r"""Sets the task_policy of this CreateBatchTask.

        :param task_policy: The task_policy of this CreateBatchTask.
        :type task_policy: :class:`huaweicloudsdkiotda.v5.TaskPolicy`
        """
        self._task_policy = task_policy

    @property
    def document_source(self):
        r"""Gets the document_source of this CreateBatchTask.

        **参数说明**：上传的批量任务文件ID。当task_type为createDevices，updateDevices，deleteDevices，freezeDevices，unfreezeDevices时，支持该参数。使用该参数时，需要先调用批量任务的文件管理接口上传文件来获取文件ID，文件样例请参见 [批量注册设备模板](https://iot-developer.obs.cn-north-4.myhuaweicloud.com/IoTM/2023-3/BatchCreateDevices_Template.xlsx)，[批量更新设备模板](https://iot-developer.obs.cn-north-4.myhuaweicloud.com/IoTM/2023-3/BatchUpdateDevices_Template.xlsx)，[批量删除设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchDeleteDevices_Template.xlsx)，[批量冻结设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchFreezeDevices_Template.xlsx)，[批量解冻设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchUnfreezeDevices_Template.xlsx)。同时使用targets、targets_filter、document_source参数时，只有一个参数会生效，且平台优先使用targets，其次是targets_filter，最后是document_source。

        :return: The document_source of this CreateBatchTask.
        :rtype: str
        """
        return self._document_source

    @document_source.setter
    def document_source(self, document_source):
        r"""Sets the document_source of this CreateBatchTask.

        **参数说明**：上传的批量任务文件ID。当task_type为createDevices，updateDevices，deleteDevices，freezeDevices，unfreezeDevices时，支持该参数。使用该参数时，需要先调用批量任务的文件管理接口上传文件来获取文件ID，文件样例请参见 [批量注册设备模板](https://iot-developer.obs.cn-north-4.myhuaweicloud.com/IoTM/2023-3/BatchCreateDevices_Template.xlsx)，[批量更新设备模板](https://iot-developer.obs.cn-north-4.myhuaweicloud.com/IoTM/2023-3/BatchUpdateDevices_Template.xlsx)，[批量删除设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchDeleteDevices_Template.xlsx)，[批量冻结设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchFreezeDevices_Template.xlsx)，[批量解冻设备模板](https://developer.obs.cn-north-4.myhuaweicloud.com/template/BatchUnfreezeDevices_Template.xlsx)。同时使用targets、targets_filter、document_source参数时，只有一个参数会生效，且平台优先使用targets，其次是targets_filter，最后是document_source。

        :param document_source: The document_source of this CreateBatchTask.
        :type document_source: str
        """
        self._document_source = document_source

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
        if not isinstance(other, CreateBatchTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
