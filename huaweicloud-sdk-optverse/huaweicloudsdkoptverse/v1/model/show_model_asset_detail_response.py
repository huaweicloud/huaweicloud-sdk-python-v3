# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowModelAssetDetailResponse(SdkResponse):

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
        'root_asset_id': 'str',
        'asset_name': 'str',
        'asset_version': 'str',
        'external_version': 'str',
        'is_available': 'str',
        'asset_location': 'str',
        'asset_desc': 'str',
        'asset_type': 'str',
        'sub_asset_type': 'str',
        'asset_code': 'str',
        'asset_source': 'str',
        'asset_actions': 'str',
        'update_time': 'int',
        'create_time': 'int',
        'creator': 'str',
        'user_id': 'str',
        'train_obs_url': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'root_asset_id': 'root_asset_id',
        'asset_name': 'asset_name',
        'asset_version': 'asset_version',
        'external_version': 'external_version',
        'is_available': 'is_available',
        'asset_location': 'asset_location',
        'asset_desc': 'asset_desc',
        'asset_type': 'asset_type',
        'sub_asset_type': 'sub_asset_type',
        'asset_code': 'asset_code',
        'asset_source': 'asset_source',
        'asset_actions': 'asset_actions',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'creator': 'creator',
        'user_id': 'user_id',
        'train_obs_url': 'train_obs_url'
    }

    def __init__(self, asset_id=None, root_asset_id=None, asset_name=None, asset_version=None, external_version=None, is_available=None, asset_location=None, asset_desc=None, asset_type=None, sub_asset_type=None, asset_code=None, asset_source=None, asset_actions=None, update_time=None, create_time=None, creator=None, user_id=None, train_obs_url=None):
        r"""ShowModelAssetDetailResponse

        The model defined in huaweicloud sdk

        :param asset_id: **参数解释**： 资产ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_id: str
        :param root_asset_id: **参数解释**： 根资产ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type root_asset_id: str
        :param asset_name: **参数解释**： 资产名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_name: str
        :param asset_version: **参数解释**： 资产内部版本。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_version: str
        :param external_version: **参数解释**： 资产对外版本。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type external_version: str
        :param is_available: **参数解释**： 对外是否可见。 **约束限制**： 不涉及 **取值范围**： * 1：可见 * 0：不可见 **默认取值**： 不涉及 
        :type is_available: str
        :param asset_location: **参数解释**： OBS存储位置。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_location: str
        :param asset_desc: **参数解释**： 资产描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_desc: str
        :param asset_type: **参数解释**： 资产类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_type: str
        :param sub_asset_type: **参数解释**： 资产子类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type sub_asset_type: str
        :param asset_code: **参数解释**： 资产编码。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_code: str
        :param asset_source: **参数解释**： 资产来源。 **约束限制**： 不涉及 **取值范围**： * Preset：预置 * AIGallery：订阅 * Import：导入 * Publish：发布 **默认取值**： 不涉及 
        :type asset_source: str
        :param asset_actions: **参数解释**： 资产应用场景，多个场景以英文逗号分隔。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type asset_actions: str
        :param update_time: **参数解释**： 更新时间（毫秒时间戳）。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type update_time: int
        :param create_time: **参数解释**： 创建时间（毫秒时间戳）。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type create_time: int
        :param creator: **参数解释**： 模型创建者名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type creator: str
        :param user_id: **参数解释**： 模型创建者ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type user_id: str
        :param train_obs_url: **参数解释**： 生成该模型时用到的数据集。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type train_obs_url: str
        """
        
        super().__init__()

        self._asset_id = None
        self._root_asset_id = None
        self._asset_name = None
        self._asset_version = None
        self._external_version = None
        self._is_available = None
        self._asset_location = None
        self._asset_desc = None
        self._asset_type = None
        self._sub_asset_type = None
        self._asset_code = None
        self._asset_source = None
        self._asset_actions = None
        self._update_time = None
        self._create_time = None
        self._creator = None
        self._user_id = None
        self._train_obs_url = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if root_asset_id is not None:
            self.root_asset_id = root_asset_id
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_version is not None:
            self.asset_version = asset_version
        if external_version is not None:
            self.external_version = external_version
        if is_available is not None:
            self.is_available = is_available
        if asset_location is not None:
            self.asset_location = asset_location
        if asset_desc is not None:
            self.asset_desc = asset_desc
        if asset_type is not None:
            self.asset_type = asset_type
        if sub_asset_type is not None:
            self.sub_asset_type = sub_asset_type
        if asset_code is not None:
            self.asset_code = asset_code
        if asset_source is not None:
            self.asset_source = asset_source
        if asset_actions is not None:
            self.asset_actions = asset_actions
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if user_id is not None:
            self.user_id = user_id
        if train_obs_url is not None:
            self.train_obs_url = train_obs_url

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ShowModelAssetDetailResponse.

        **参数解释**： 资产ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_id of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ShowModelAssetDetailResponse.

        **参数解释**： 资产ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_id: The asset_id of this ShowModelAssetDetailResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def root_asset_id(self):
        r"""Gets the root_asset_id of this ShowModelAssetDetailResponse.

        **参数解释**： 根资产ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The root_asset_id of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._root_asset_id

    @root_asset_id.setter
    def root_asset_id(self, root_asset_id):
        r"""Sets the root_asset_id of this ShowModelAssetDetailResponse.

        **参数解释**： 根资产ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param root_asset_id: The root_asset_id of this ShowModelAssetDetailResponse.
        :type root_asset_id: str
        """
        self._root_asset_id = root_asset_id

    @property
    def asset_name(self):
        r"""Gets the asset_name of this ShowModelAssetDetailResponse.

        **参数解释**： 资产名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_name of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this ShowModelAssetDetailResponse.

        **参数解释**： 资产名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_name: The asset_name of this ShowModelAssetDetailResponse.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_version(self):
        r"""Gets the asset_version of this ShowModelAssetDetailResponse.

        **参数解释**： 资产内部版本。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_version of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        r"""Sets the asset_version of this ShowModelAssetDetailResponse.

        **参数解释**： 资产内部版本。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_version: The asset_version of this ShowModelAssetDetailResponse.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def external_version(self):
        r"""Gets the external_version of this ShowModelAssetDetailResponse.

        **参数解释**： 资产对外版本。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The external_version of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._external_version

    @external_version.setter
    def external_version(self, external_version):
        r"""Sets the external_version of this ShowModelAssetDetailResponse.

        **参数解释**： 资产对外版本。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param external_version: The external_version of this ShowModelAssetDetailResponse.
        :type external_version: str
        """
        self._external_version = external_version

    @property
    def is_available(self):
        r"""Gets the is_available of this ShowModelAssetDetailResponse.

        **参数解释**： 对外是否可见。 **约束限制**： 不涉及 **取值范围**： * 1：可见 * 0：不可见 **默认取值**： 不涉及 

        :return: The is_available of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        r"""Sets the is_available of this ShowModelAssetDetailResponse.

        **参数解释**： 对外是否可见。 **约束限制**： 不涉及 **取值范围**： * 1：可见 * 0：不可见 **默认取值**： 不涉及 

        :param is_available: The is_available of this ShowModelAssetDetailResponse.
        :type is_available: str
        """
        self._is_available = is_available

    @property
    def asset_location(self):
        r"""Gets the asset_location of this ShowModelAssetDetailResponse.

        **参数解释**： OBS存储位置。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_location of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._asset_location

    @asset_location.setter
    def asset_location(self, asset_location):
        r"""Sets the asset_location of this ShowModelAssetDetailResponse.

        **参数解释**： OBS存储位置。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_location: The asset_location of this ShowModelAssetDetailResponse.
        :type asset_location: str
        """
        self._asset_location = asset_location

    @property
    def asset_desc(self):
        r"""Gets the asset_desc of this ShowModelAssetDetailResponse.

        **参数解释**： 资产描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_desc of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._asset_desc

    @asset_desc.setter
    def asset_desc(self, asset_desc):
        r"""Sets the asset_desc of this ShowModelAssetDetailResponse.

        **参数解释**： 资产描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_desc: The asset_desc of this ShowModelAssetDetailResponse.
        :type asset_desc: str
        """
        self._asset_desc = asset_desc

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ShowModelAssetDetailResponse.

        **参数解释**： 资产类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_type of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ShowModelAssetDetailResponse.

        **参数解释**： 资产类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_type: The asset_type of this ShowModelAssetDetailResponse.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def sub_asset_type(self):
        r"""Gets the sub_asset_type of this ShowModelAssetDetailResponse.

        **参数解释**： 资产子类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The sub_asset_type of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._sub_asset_type

    @sub_asset_type.setter
    def sub_asset_type(self, sub_asset_type):
        r"""Sets the sub_asset_type of this ShowModelAssetDetailResponse.

        **参数解释**： 资产子类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param sub_asset_type: The sub_asset_type of this ShowModelAssetDetailResponse.
        :type sub_asset_type: str
        """
        self._sub_asset_type = sub_asset_type

    @property
    def asset_code(self):
        r"""Gets the asset_code of this ShowModelAssetDetailResponse.

        **参数解释**： 资产编码。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_code of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this ShowModelAssetDetailResponse.

        **参数解释**： 资产编码。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_code: The asset_code of this ShowModelAssetDetailResponse.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def asset_source(self):
        r"""Gets the asset_source of this ShowModelAssetDetailResponse.

        **参数解释**： 资产来源。 **约束限制**： 不涉及 **取值范围**： * Preset：预置 * AIGallery：订阅 * Import：导入 * Publish：发布 **默认取值**： 不涉及 

        :return: The asset_source of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._asset_source

    @asset_source.setter
    def asset_source(self, asset_source):
        r"""Sets the asset_source of this ShowModelAssetDetailResponse.

        **参数解释**： 资产来源。 **约束限制**： 不涉及 **取值范围**： * Preset：预置 * AIGallery：订阅 * Import：导入 * Publish：发布 **默认取值**： 不涉及 

        :param asset_source: The asset_source of this ShowModelAssetDetailResponse.
        :type asset_source: str
        """
        self._asset_source = asset_source

    @property
    def asset_actions(self):
        r"""Gets the asset_actions of this ShowModelAssetDetailResponse.

        **参数解释**： 资产应用场景，多个场景以英文逗号分隔。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The asset_actions of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._asset_actions

    @asset_actions.setter
    def asset_actions(self, asset_actions):
        r"""Sets the asset_actions of this ShowModelAssetDetailResponse.

        **参数解释**： 资产应用场景，多个场景以英文逗号分隔。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param asset_actions: The asset_actions of this ShowModelAssetDetailResponse.
        :type asset_actions: str
        """
        self._asset_actions = asset_actions

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowModelAssetDetailResponse.

        **参数解释**： 更新时间（毫秒时间戳）。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The update_time of this ShowModelAssetDetailResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowModelAssetDetailResponse.

        **参数解释**： 更新时间（毫秒时间戳）。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param update_time: The update_time of this ShowModelAssetDetailResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowModelAssetDetailResponse.

        **参数解释**： 创建时间（毫秒时间戳）。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The create_time of this ShowModelAssetDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowModelAssetDetailResponse.

        **参数解释**： 创建时间（毫秒时间戳）。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param create_time: The create_time of this ShowModelAssetDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this ShowModelAssetDetailResponse.

        **参数解释**： 模型创建者名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The creator of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowModelAssetDetailResponse.

        **参数解释**： 模型创建者名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param creator: The creator of this ShowModelAssetDetailResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowModelAssetDetailResponse.

        **参数解释**： 模型创建者ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The user_id of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowModelAssetDetailResponse.

        **参数解释**： 模型创建者ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param user_id: The user_id of this ShowModelAssetDetailResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def train_obs_url(self):
        r"""Gets the train_obs_url of this ShowModelAssetDetailResponse.

        **参数解释**： 生成该模型时用到的数据集。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The train_obs_url of this ShowModelAssetDetailResponse.
        :rtype: str
        """
        return self._train_obs_url

    @train_obs_url.setter
    def train_obs_url(self, train_obs_url):
        r"""Sets the train_obs_url of this ShowModelAssetDetailResponse.

        **参数解释**： 生成该模型时用到的数据集。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param train_obs_url: The train_obs_url of this ShowModelAssetDetailResponse.
        :type train_obs_url: str
        """
        self._train_obs_url = train_obs_url

    def to_dict(self):
        import warnings
        warnings.warn("ShowModelAssetDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowModelAssetDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
