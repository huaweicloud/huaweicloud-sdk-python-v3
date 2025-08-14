# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DigitalAssetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'asset_id': 'str',
        'produce_id': 'str',
        'asset_name': 'str',
        'asset_description': 'str',
        'app_user_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'asset_type': 'str',
        'asset_state': 'str',
        'fail_type': 'str',
        'block_reason_code': 'str',
        'reason': 'str',
        'tags': 'list[str]',
        'asset_extra_meta': 'AssetExtraMeta',
        'system_properties': 'list[SystemProperty]',
        'files': 'list[AssetFileInfo]',
        'asset_order': 'int',
        'supported_service': 'list[SupportedServiceEnum]',
        'auto_operation_config': 'list[AutoOperationConfig]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'asset_id': 'asset_id',
        'produce_id': 'produce_id',
        'asset_name': 'asset_name',
        'asset_description': 'asset_description',
        'app_user_id': 'app_user_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'asset_type': 'asset_type',
        'asset_state': 'asset_state',
        'fail_type': 'fail_type',
        'block_reason_code': 'block_reason_code',
        'reason': 'reason',
        'tags': 'tags',
        'asset_extra_meta': 'asset_extra_meta',
        'system_properties': 'system_properties',
        'files': 'files',
        'asset_order': 'asset_order',
        'supported_service': 'supported_service',
        'auto_operation_config': 'auto_operation_config'
    }

    def __init__(self, project_id=None, asset_id=None, produce_id=None, asset_name=None, asset_description=None, app_user_id=None, create_time=None, update_time=None, asset_type=None, asset_state=None, fail_type=None, block_reason_code=None, reason=None, tags=None, asset_extra_meta=None, system_properties=None, files=None, asset_order=None, supported_service=None, auto_operation_config=None):
        r"""DigitalAssetInfo

        The model defined in huaweicloud sdk

        :param project_id: 租户id
        :type project_id: str
        :param asset_id: 资产ID。
        :type asset_id: str
        :param produce_id: ai标识ID。
        :type produce_id: str
        :param asset_name: 资产名称。
        :type asset_name: str
        :param asset_description: 资产描述。
        :type asset_description: str
        :param app_user_id: 第三方用户ID。 &gt; * 即创建资产是通过X-App-UserId头域传入的值。
        :type app_user_id: str
        :param create_time: 资产创建时间。
        :type create_time: str
        :param update_time: 资产更新时间。
        :type update_time: str
        :param asset_type: 资产类型。  公共资产类型： * VOICE_MODEL：音色模型 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产类型： * HUMAN_MODEL_2D：分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板
        :type asset_type: str
        :param asset_state: 资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。 * WAITING_DELETE：资产将被下线
        :type asset_state: str
        :param fail_type: 失败原因。 * AUTOMATIC_REVIEW_REJECT：自动审核失败 * MANUAL_REVIEW_REJECT：人工审核失败
        :type fail_type: str
        :param block_reason_code: 冻结原因编号。
        :type block_reason_code: str
        :param reason: 冻结/解冻/失败 原因。
        :type reason: str
        :param tags: 标签列表。 &gt; 分身形象系统资产的tag定义如下： &gt; - 行业：NEWS,BUSINESS,E-COMMERCE,MARKETING,KNOWLEDGE,EDUCATION,SPORTS &gt; - 性别：MALE,FEMALE &gt; - 姿势：FULL-BODY,HALF-BODY,STANDING,SITTING,WALKING &gt; - 区域：ASIAN,WESTERN,MIDDLE-EASTERNER,AFRICAN,LATINO
        :type tags: list[str]
        :param asset_extra_meta: 
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        :param system_properties: 设置系统属性。
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        :param files: 资产下的文件。
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.AssetFileInfo`]
        :param asset_order: 展示顺序
        :type asset_order: int
        :param supported_service: 支持的业务类型。： * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        :param auto_operation_config: 资产自动处理任务。
        :type auto_operation_config: list[:class:`huaweicloudsdkmetastudio.v1.AutoOperationConfig`]
        """
        
        

        self._project_id = None
        self._asset_id = None
        self._produce_id = None
        self._asset_name = None
        self._asset_description = None
        self._app_user_id = None
        self._create_time = None
        self._update_time = None
        self._asset_type = None
        self._asset_state = None
        self._fail_type = None
        self._block_reason_code = None
        self._reason = None
        self._tags = None
        self._asset_extra_meta = None
        self._system_properties = None
        self._files = None
        self._asset_order = None
        self._supported_service = None
        self._auto_operation_config = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if asset_id is not None:
            self.asset_id = asset_id
        if produce_id is not None:
            self.produce_id = produce_id
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_description is not None:
            self.asset_description = asset_description
        if app_user_id is not None:
            self.app_user_id = app_user_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_state is not None:
            self.asset_state = asset_state
        if fail_type is not None:
            self.fail_type = fail_type
        if block_reason_code is not None:
            self.block_reason_code = block_reason_code
        if reason is not None:
            self.reason = reason
        if tags is not None:
            self.tags = tags
        if asset_extra_meta is not None:
            self.asset_extra_meta = asset_extra_meta
        if system_properties is not None:
            self.system_properties = system_properties
        if files is not None:
            self.files = files
        if asset_order is not None:
            self.asset_order = asset_order
        if supported_service is not None:
            self.supported_service = supported_service
        if auto_operation_config is not None:
            self.auto_operation_config = auto_operation_config

    @property
    def project_id(self):
        r"""Gets the project_id of this DigitalAssetInfo.

        租户id

        :return: The project_id of this DigitalAssetInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DigitalAssetInfo.

        租户id

        :param project_id: The project_id of this DigitalAssetInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def asset_id(self):
        r"""Gets the asset_id of this DigitalAssetInfo.

        资产ID。

        :return: The asset_id of this DigitalAssetInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this DigitalAssetInfo.

        资产ID。

        :param asset_id: The asset_id of this DigitalAssetInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def produce_id(self):
        r"""Gets the produce_id of this DigitalAssetInfo.

        ai标识ID。

        :return: The produce_id of this DigitalAssetInfo.
        :rtype: str
        """
        return self._produce_id

    @produce_id.setter
    def produce_id(self, produce_id):
        r"""Sets the produce_id of this DigitalAssetInfo.

        ai标识ID。

        :param produce_id: The produce_id of this DigitalAssetInfo.
        :type produce_id: str
        """
        self._produce_id = produce_id

    @property
    def asset_name(self):
        r"""Gets the asset_name of this DigitalAssetInfo.

        资产名称。

        :return: The asset_name of this DigitalAssetInfo.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this DigitalAssetInfo.

        资产名称。

        :param asset_name: The asset_name of this DigitalAssetInfo.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_description(self):
        r"""Gets the asset_description of this DigitalAssetInfo.

        资产描述。

        :return: The asset_description of this DigitalAssetInfo.
        :rtype: str
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        r"""Sets the asset_description of this DigitalAssetInfo.

        资产描述。

        :param asset_description: The asset_description of this DigitalAssetInfo.
        :type asset_description: str
        """
        self._asset_description = asset_description

    @property
    def app_user_id(self):
        r"""Gets the app_user_id of this DigitalAssetInfo.

        第三方用户ID。 > * 即创建资产是通过X-App-UserId头域传入的值。

        :return: The app_user_id of this DigitalAssetInfo.
        :rtype: str
        """
        return self._app_user_id

    @app_user_id.setter
    def app_user_id(self, app_user_id):
        r"""Sets the app_user_id of this DigitalAssetInfo.

        第三方用户ID。 > * 即创建资产是通过X-App-UserId头域传入的值。

        :param app_user_id: The app_user_id of this DigitalAssetInfo.
        :type app_user_id: str
        """
        self._app_user_id = app_user_id

    @property
    def create_time(self):
        r"""Gets the create_time of this DigitalAssetInfo.

        资产创建时间。

        :return: The create_time of this DigitalAssetInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DigitalAssetInfo.

        资产创建时间。

        :param create_time: The create_time of this DigitalAssetInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this DigitalAssetInfo.

        资产更新时间。

        :return: The update_time of this DigitalAssetInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DigitalAssetInfo.

        资产更新时间。

        :param update_time: The update_time of this DigitalAssetInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def asset_type(self):
        r"""Gets the asset_type of this DigitalAssetInfo.

        资产类型。  公共资产类型： * VOICE_MODEL：音色模型 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产类型： * HUMAN_MODEL_2D：分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板

        :return: The asset_type of this DigitalAssetInfo.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this DigitalAssetInfo.

        资产类型。  公共资产类型： * VOICE_MODEL：音色模型 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产类型： * HUMAN_MODEL_2D：分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板

        :param asset_type: The asset_type of this DigitalAssetInfo.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_state(self):
        r"""Gets the asset_state of this DigitalAssetInfo.

        资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。 * WAITING_DELETE：资产将被下线

        :return: The asset_state of this DigitalAssetInfo.
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        r"""Sets the asset_state of this DigitalAssetInfo.

        资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。 * WAITING_DELETE：资产将被下线

        :param asset_state: The asset_state of this DigitalAssetInfo.
        :type asset_state: str
        """
        self._asset_state = asset_state

    @property
    def fail_type(self):
        r"""Gets the fail_type of this DigitalAssetInfo.

        失败原因。 * AUTOMATIC_REVIEW_REJECT：自动审核失败 * MANUAL_REVIEW_REJECT：人工审核失败

        :return: The fail_type of this DigitalAssetInfo.
        :rtype: str
        """
        return self._fail_type

    @fail_type.setter
    def fail_type(self, fail_type):
        r"""Sets the fail_type of this DigitalAssetInfo.

        失败原因。 * AUTOMATIC_REVIEW_REJECT：自动审核失败 * MANUAL_REVIEW_REJECT：人工审核失败

        :param fail_type: The fail_type of this DigitalAssetInfo.
        :type fail_type: str
        """
        self._fail_type = fail_type

    @property
    def block_reason_code(self):
        r"""Gets the block_reason_code of this DigitalAssetInfo.

        冻结原因编号。

        :return: The block_reason_code of this DigitalAssetInfo.
        :rtype: str
        """
        return self._block_reason_code

    @block_reason_code.setter
    def block_reason_code(self, block_reason_code):
        r"""Sets the block_reason_code of this DigitalAssetInfo.

        冻结原因编号。

        :param block_reason_code: The block_reason_code of this DigitalAssetInfo.
        :type block_reason_code: str
        """
        self._block_reason_code = block_reason_code

    @property
    def reason(self):
        r"""Gets the reason of this DigitalAssetInfo.

        冻结/解冻/失败 原因。

        :return: The reason of this DigitalAssetInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this DigitalAssetInfo.

        冻结/解冻/失败 原因。

        :param reason: The reason of this DigitalAssetInfo.
        :type reason: str
        """
        self._reason = reason

    @property
    def tags(self):
        r"""Gets the tags of this DigitalAssetInfo.

        标签列表。 > 分身形象系统资产的tag定义如下： > - 行业：NEWS,BUSINESS,E-COMMERCE,MARKETING,KNOWLEDGE,EDUCATION,SPORTS > - 性别：MALE,FEMALE > - 姿势：FULL-BODY,HALF-BODY,STANDING,SITTING,WALKING > - 区域：ASIAN,WESTERN,MIDDLE-EASTERNER,AFRICAN,LATINO

        :return: The tags of this DigitalAssetInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this DigitalAssetInfo.

        标签列表。 > 分身形象系统资产的tag定义如下： > - 行业：NEWS,BUSINESS,E-COMMERCE,MARKETING,KNOWLEDGE,EDUCATION,SPORTS > - 性别：MALE,FEMALE > - 姿势：FULL-BODY,HALF-BODY,STANDING,SITTING,WALKING > - 区域：ASIAN,WESTERN,MIDDLE-EASTERNER,AFRICAN,LATINO

        :param tags: The tags of this DigitalAssetInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def asset_extra_meta(self):
        r"""Gets the asset_extra_meta of this DigitalAssetInfo.

        :return: The asset_extra_meta of this DigitalAssetInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        return self._asset_extra_meta

    @asset_extra_meta.setter
    def asset_extra_meta(self, asset_extra_meta):
        r"""Sets the asset_extra_meta of this DigitalAssetInfo.

        :param asset_extra_meta: The asset_extra_meta of this DigitalAssetInfo.
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        self._asset_extra_meta = asset_extra_meta

    @property
    def system_properties(self):
        r"""Gets the system_properties of this DigitalAssetInfo.

        设置系统属性。

        :return: The system_properties of this DigitalAssetInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        return self._system_properties

    @system_properties.setter
    def system_properties(self, system_properties):
        r"""Sets the system_properties of this DigitalAssetInfo.

        设置系统属性。

        :param system_properties: The system_properties of this DigitalAssetInfo.
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        self._system_properties = system_properties

    @property
    def files(self):
        r"""Gets the files of this DigitalAssetInfo.

        资产下的文件。

        :return: The files of this DigitalAssetInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AssetFileInfo`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this DigitalAssetInfo.

        资产下的文件。

        :param files: The files of this DigitalAssetInfo.
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.AssetFileInfo`]
        """
        self._files = files

    @property
    def asset_order(self):
        r"""Gets the asset_order of this DigitalAssetInfo.

        展示顺序

        :return: The asset_order of this DigitalAssetInfo.
        :rtype: int
        """
        return self._asset_order

    @asset_order.setter
    def asset_order(self, asset_order):
        r"""Sets the asset_order of this DigitalAssetInfo.

        展示顺序

        :param asset_order: The asset_order of this DigitalAssetInfo.
        :type asset_order: int
        """
        self._asset_order = asset_order

    @property
    def supported_service(self):
        r"""Gets the supported_service of this DigitalAssetInfo.

        支持的业务类型。： * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互

        :return: The supported_service of this DigitalAssetInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        return self._supported_service

    @supported_service.setter
    def supported_service(self, supported_service):
        r"""Sets the supported_service of this DigitalAssetInfo.

        支持的业务类型。： * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互

        :param supported_service: The supported_service of this DigitalAssetInfo.
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        self._supported_service = supported_service

    @property
    def auto_operation_config(self):
        r"""Gets the auto_operation_config of this DigitalAssetInfo.

        资产自动处理任务。

        :return: The auto_operation_config of this DigitalAssetInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AutoOperationConfig`]
        """
        return self._auto_operation_config

    @auto_operation_config.setter
    def auto_operation_config(self, auto_operation_config):
        r"""Sets the auto_operation_config of this DigitalAssetInfo.

        资产自动处理任务。

        :param auto_operation_config: The auto_operation_config of this DigitalAssetInfo.
        :type auto_operation_config: list[:class:`huaweicloudsdkmetastudio.v1.AutoOperationConfig`]
        """
        self._auto_operation_config = auto_operation_config

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
        if not isinstance(other, DigitalAssetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
