# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDigitalAssetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'asset_name': 'str',
        'asset_description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'asset_type': 'str',
        'asset_state': 'str',
        'tags': 'list[str]',
        'asset_extra_meta': 'AssetExtraMeta',
        'system_properties': 'list[SystemProperty]',
        'files': 'list[AssetFileInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_name': 'asset_name',
        'asset_description': 'asset_description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'asset_type': 'asset_type',
        'asset_state': 'asset_state',
        'tags': 'tags',
        'asset_extra_meta': 'asset_extra_meta',
        'system_properties': 'system_properties',
        'files': 'files',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, asset_id=None, asset_name=None, asset_description=None, create_time=None, update_time=None, asset_type=None, asset_state=None, tags=None, asset_extra_meta=None, system_properties=None, files=None, x_request_id=None):
        """UpdateDigitalAssetResponse

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID。
        :type asset_id: str
        :param asset_name: 资产名称。
        :type asset_name: str
        :param asset_description: 资产描述。
        :type asset_description: str
        :param create_time: 资产创建时间。
        :type create_time: str
        :param update_time: 资产更新时间。
        :type update_time: str
        :param asset_type: 资产类型。 * HUMAN_MODEL：数字人模型 * VOICE_MODEL：音色模型 * SCENE：场景模型 * ANIMATION：动作动画 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型 * COMMON_FILE：通用文件 * HUMAN_MODEL_2D:2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐
        :type asset_type: str
        :param asset_state: 资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。
        :type asset_state: str
        :param tags: 标签列表。
        :type tags: list[str]
        :param asset_extra_meta: 
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        :param system_properties: 设置系统属性。
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        :param files: 资产下的文件。
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.AssetFileInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateDigitalAssetResponse, self).__init__()

        self._asset_id = None
        self._asset_name = None
        self._asset_description = None
        self._create_time = None
        self._update_time = None
        self._asset_type = None
        self._asset_state = None
        self._tags = None
        self._asset_extra_meta = None
        self._system_properties = None
        self._files = None
        self._x_request_id = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_description is not None:
            self.asset_description = asset_description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_state is not None:
            self.asset_state = asset_state
        if tags is not None:
            self.tags = tags
        if asset_extra_meta is not None:
            self.asset_extra_meta = asset_extra_meta
        if system_properties is not None:
            self.system_properties = system_properties
        if files is not None:
            self.files = files
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def asset_id(self):
        """Gets the asset_id of this UpdateDigitalAssetResponse.

        资产ID。

        :return: The asset_id of this UpdateDigitalAssetResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this UpdateDigitalAssetResponse.

        资产ID。

        :param asset_id: The asset_id of this UpdateDigitalAssetResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_name(self):
        """Gets the asset_name of this UpdateDigitalAssetResponse.

        资产名称。

        :return: The asset_name of this UpdateDigitalAssetResponse.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this UpdateDigitalAssetResponse.

        资产名称。

        :param asset_name: The asset_name of this UpdateDigitalAssetResponse.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_description(self):
        """Gets the asset_description of this UpdateDigitalAssetResponse.

        资产描述。

        :return: The asset_description of this UpdateDigitalAssetResponse.
        :rtype: str
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        """Sets the asset_description of this UpdateDigitalAssetResponse.

        资产描述。

        :param asset_description: The asset_description of this UpdateDigitalAssetResponse.
        :type asset_description: str
        """
        self._asset_description = asset_description

    @property
    def create_time(self):
        """Gets the create_time of this UpdateDigitalAssetResponse.

        资产创建时间。

        :return: The create_time of this UpdateDigitalAssetResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateDigitalAssetResponse.

        资产创建时间。

        :param create_time: The create_time of this UpdateDigitalAssetResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UpdateDigitalAssetResponse.

        资产更新时间。

        :return: The update_time of this UpdateDigitalAssetResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateDigitalAssetResponse.

        资产更新时间。

        :param update_time: The update_time of this UpdateDigitalAssetResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def asset_type(self):
        """Gets the asset_type of this UpdateDigitalAssetResponse.

        资产类型。 * HUMAN_MODEL：数字人模型 * VOICE_MODEL：音色模型 * SCENE：场景模型 * ANIMATION：动作动画 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型 * COMMON_FILE：通用文件 * HUMAN_MODEL_2D:2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐

        :return: The asset_type of this UpdateDigitalAssetResponse.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this UpdateDigitalAssetResponse.

        资产类型。 * HUMAN_MODEL：数字人模型 * VOICE_MODEL：音色模型 * SCENE：场景模型 * ANIMATION：动作动画 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型 * COMMON_FILE：通用文件 * HUMAN_MODEL_2D:2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐

        :param asset_type: The asset_type of this UpdateDigitalAssetResponse.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_state(self):
        """Gets the asset_state of this UpdateDigitalAssetResponse.

        资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。

        :return: The asset_state of this UpdateDigitalAssetResponse.
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        """Sets the asset_state of this UpdateDigitalAssetResponse.

        资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。

        :param asset_state: The asset_state of this UpdateDigitalAssetResponse.
        :type asset_state: str
        """
        self._asset_state = asset_state

    @property
    def tags(self):
        """Gets the tags of this UpdateDigitalAssetResponse.

        标签列表。

        :return: The tags of this UpdateDigitalAssetResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateDigitalAssetResponse.

        标签列表。

        :param tags: The tags of this UpdateDigitalAssetResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def asset_extra_meta(self):
        """Gets the asset_extra_meta of this UpdateDigitalAssetResponse.

        :return: The asset_extra_meta of this UpdateDigitalAssetResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        return self._asset_extra_meta

    @asset_extra_meta.setter
    def asset_extra_meta(self, asset_extra_meta):
        """Sets the asset_extra_meta of this UpdateDigitalAssetResponse.

        :param asset_extra_meta: The asset_extra_meta of this UpdateDigitalAssetResponse.
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        self._asset_extra_meta = asset_extra_meta

    @property
    def system_properties(self):
        """Gets the system_properties of this UpdateDigitalAssetResponse.

        设置系统属性。

        :return: The system_properties of this UpdateDigitalAssetResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        return self._system_properties

    @system_properties.setter
    def system_properties(self, system_properties):
        """Sets the system_properties of this UpdateDigitalAssetResponse.

        设置系统属性。

        :param system_properties: The system_properties of this UpdateDigitalAssetResponse.
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        self._system_properties = system_properties

    @property
    def files(self):
        """Gets the files of this UpdateDigitalAssetResponse.

        资产下的文件。

        :return: The files of this UpdateDigitalAssetResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AssetFileInfo`]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this UpdateDigitalAssetResponse.

        资产下的文件。

        :param files: The files of this UpdateDigitalAssetResponse.
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.AssetFileInfo`]
        """
        self._files = files

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateDigitalAssetResponse.

        :return: The x_request_id of this UpdateDigitalAssetResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateDigitalAssetResponse.

        :param x_request_id: The x_request_id of this UpdateDigitalAssetResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateDigitalAssetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
