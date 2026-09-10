# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelServiceRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'service_name': 'str',
        'service_desc': 'str',
        'status': 'str',
        'infer_type': 'str',
        'device_type': 'str',
        'chip_type': 'str',
        'request_mode': 'str',
        'asset_id': 'str',
        'asset_name': 'str',
        'asset_type': 'str',
        'asset_sub_type': 'str',
        'api_url': 'str',
        'chat_id': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'platform': 'str',
        'train_obs_output': 'str',
        'use_type': 'str',
        'service_config': 'ModelServiceConfig',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'service_id': 'service_id',
        'service_name': 'service_name',
        'service_desc': 'service_desc',
        'status': 'status',
        'infer_type': 'infer_type',
        'device_type': 'device_type',
        'chip_type': 'chip_type',
        'request_mode': 'request_mode',
        'asset_id': 'asset_id',
        'asset_name': 'asset_name',
        'asset_type': 'asset_type',
        'asset_sub_type': 'asset_sub_type',
        'api_url': 'api_url',
        'chat_id': 'chat_id',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'platform': 'platform',
        'train_obs_output': 'train_obs_output',
        'use_type': 'use_type',
        'service_config': 'service_config',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, service_id=None, service_name=None, service_desc=None, status=None, infer_type=None, device_type=None, chip_type=None, request_mode=None, asset_id=None, asset_name=None, asset_type=None, asset_sub_type=None, api_url=None, chat_id=None, user_id=None, user_name=None, platform=None, train_obs_output=None, use_type=None, service_config=None, create_time=None, update_time=None):
        r"""ModelServiceRsp

        The model defined in huaweicloud sdk

        :param service_id: 服务ID
        :type service_id: str
        :param service_name: 服务名称
        :type service_name: str
        :param service_desc: 服务描述
        :type service_desc: str
        :param status: 服务状态，INIT/RUNNING/STOPPED/FAILED
        :type status: str
        :param infer_type: 推理类型，分为online和edge
        :type infer_type: str
        :param device_type: 设备类型
        :type device_type: str
        :param chip_type: 芯片类型
        :type chip_type: str
        :param request_mode: 请求类型
        :type request_mode: str
        :param asset_id: 推理服务所关联的模型ID
        :type asset_id: str
        :param asset_name: 推理服务所关联的模型名称
        :type asset_name: str
        :param asset_type: 推理服务所关联的模型类型
        :type asset_type: str
        :param asset_sub_type: 推理服务所关联的模型子类型
        :type asset_sub_type: str
        :param api_url: API调用地址
        :type api_url: str
        :param chat_id: 关联对话ID
        :type chat_id: str
        :param user_id: 模型部署服务的用户ID
        :type user_id: str
        :param user_name: 模型部署服务的用户名称
        :type user_name: str
        :param platform: 部署平台，Modelarts或者CCE
        :type platform: str
        :param train_obs_output: 训练产物OBS地址
        :type train_obs_output: str
        :param use_type: 使用类型，private表示用户创建的服务，public表示预置服务
        :type use_type: str
        :param service_config: 
        :type service_config: :class:`huaweicloudsdkoptverse.v1.ModelServiceConfig`
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        """
        
        

        self._service_id = None
        self._service_name = None
        self._service_desc = None
        self._status = None
        self._infer_type = None
        self._device_type = None
        self._chip_type = None
        self._request_mode = None
        self._asset_id = None
        self._asset_name = None
        self._asset_type = None
        self._asset_sub_type = None
        self._api_url = None
        self._chat_id = None
        self._user_id = None
        self._user_name = None
        self._platform = None
        self._train_obs_output = None
        self._use_type = None
        self._service_config = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.service_id = service_id
        self.service_name = service_name
        if service_desc is not None:
            self.service_desc = service_desc
        self.status = status
        self.infer_type = infer_type
        if device_type is not None:
            self.device_type = device_type
        if chip_type is not None:
            self.chip_type = chip_type
        if request_mode is not None:
            self.request_mode = request_mode
        self.asset_id = asset_id
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_sub_type is not None:
            self.asset_sub_type = asset_sub_type
        if api_url is not None:
            self.api_url = api_url
        if chat_id is not None:
            self.chat_id = chat_id
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        self.platform = platform
        if train_obs_output is not None:
            self.train_obs_output = train_obs_output
        if use_type is not None:
            self.use_type = use_type
        if service_config is not None:
            self.service_config = service_config
        self.create_time = create_time
        self.update_time = update_time

    @property
    def service_id(self):
        r"""Gets the service_id of this ModelServiceRsp.

        服务ID

        :return: The service_id of this ModelServiceRsp.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ModelServiceRsp.

        服务ID

        :param service_id: The service_id of this ModelServiceRsp.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_name(self):
        r"""Gets the service_name of this ModelServiceRsp.

        服务名称

        :return: The service_name of this ModelServiceRsp.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ModelServiceRsp.

        服务名称

        :param service_name: The service_name of this ModelServiceRsp.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def service_desc(self):
        r"""Gets the service_desc of this ModelServiceRsp.

        服务描述

        :return: The service_desc of this ModelServiceRsp.
        :rtype: str
        """
        return self._service_desc

    @service_desc.setter
    def service_desc(self, service_desc):
        r"""Sets the service_desc of this ModelServiceRsp.

        服务描述

        :param service_desc: The service_desc of this ModelServiceRsp.
        :type service_desc: str
        """
        self._service_desc = service_desc

    @property
    def status(self):
        r"""Gets the status of this ModelServiceRsp.

        服务状态，INIT/RUNNING/STOPPED/FAILED

        :return: The status of this ModelServiceRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ModelServiceRsp.

        服务状态，INIT/RUNNING/STOPPED/FAILED

        :param status: The status of this ModelServiceRsp.
        :type status: str
        """
        self._status = status

    @property
    def infer_type(self):
        r"""Gets the infer_type of this ModelServiceRsp.

        推理类型，分为online和edge

        :return: The infer_type of this ModelServiceRsp.
        :rtype: str
        """
        return self._infer_type

    @infer_type.setter
    def infer_type(self, infer_type):
        r"""Sets the infer_type of this ModelServiceRsp.

        推理类型，分为online和edge

        :param infer_type: The infer_type of this ModelServiceRsp.
        :type infer_type: str
        """
        self._infer_type = infer_type

    @property
    def device_type(self):
        r"""Gets the device_type of this ModelServiceRsp.

        设备类型

        :return: The device_type of this ModelServiceRsp.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        r"""Sets the device_type of this ModelServiceRsp.

        设备类型

        :param device_type: The device_type of this ModelServiceRsp.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def chip_type(self):
        r"""Gets the chip_type of this ModelServiceRsp.

        芯片类型

        :return: The chip_type of this ModelServiceRsp.
        :rtype: str
        """
        return self._chip_type

    @chip_type.setter
    def chip_type(self, chip_type):
        r"""Sets the chip_type of this ModelServiceRsp.

        芯片类型

        :param chip_type: The chip_type of this ModelServiceRsp.
        :type chip_type: str
        """
        self._chip_type = chip_type

    @property
    def request_mode(self):
        r"""Gets the request_mode of this ModelServiceRsp.

        请求类型

        :return: The request_mode of this ModelServiceRsp.
        :rtype: str
        """
        return self._request_mode

    @request_mode.setter
    def request_mode(self, request_mode):
        r"""Sets the request_mode of this ModelServiceRsp.

        请求类型

        :param request_mode: The request_mode of this ModelServiceRsp.
        :type request_mode: str
        """
        self._request_mode = request_mode

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ModelServiceRsp.

        推理服务所关联的模型ID

        :return: The asset_id of this ModelServiceRsp.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ModelServiceRsp.

        推理服务所关联的模型ID

        :param asset_id: The asset_id of this ModelServiceRsp.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_name(self):
        r"""Gets the asset_name of this ModelServiceRsp.

        推理服务所关联的模型名称

        :return: The asset_name of this ModelServiceRsp.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this ModelServiceRsp.

        推理服务所关联的模型名称

        :param asset_name: The asset_name of this ModelServiceRsp.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ModelServiceRsp.

        推理服务所关联的模型类型

        :return: The asset_type of this ModelServiceRsp.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ModelServiceRsp.

        推理服务所关联的模型类型

        :param asset_type: The asset_type of this ModelServiceRsp.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_sub_type(self):
        r"""Gets the asset_sub_type of this ModelServiceRsp.

        推理服务所关联的模型子类型

        :return: The asset_sub_type of this ModelServiceRsp.
        :rtype: str
        """
        return self._asset_sub_type

    @asset_sub_type.setter
    def asset_sub_type(self, asset_sub_type):
        r"""Sets the asset_sub_type of this ModelServiceRsp.

        推理服务所关联的模型子类型

        :param asset_sub_type: The asset_sub_type of this ModelServiceRsp.
        :type asset_sub_type: str
        """
        self._asset_sub_type = asset_sub_type

    @property
    def api_url(self):
        r"""Gets the api_url of this ModelServiceRsp.

        API调用地址

        :return: The api_url of this ModelServiceRsp.
        :rtype: str
        """
        return self._api_url

    @api_url.setter
    def api_url(self, api_url):
        r"""Sets the api_url of this ModelServiceRsp.

        API调用地址

        :param api_url: The api_url of this ModelServiceRsp.
        :type api_url: str
        """
        self._api_url = api_url

    @property
    def chat_id(self):
        r"""Gets the chat_id of this ModelServiceRsp.

        关联对话ID

        :return: The chat_id of this ModelServiceRsp.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        r"""Sets the chat_id of this ModelServiceRsp.

        关联对话ID

        :param chat_id: The chat_id of this ModelServiceRsp.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def user_id(self):
        r"""Gets the user_id of this ModelServiceRsp.

        模型部署服务的用户ID

        :return: The user_id of this ModelServiceRsp.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ModelServiceRsp.

        模型部署服务的用户ID

        :param user_id: The user_id of this ModelServiceRsp.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ModelServiceRsp.

        模型部署服务的用户名称

        :return: The user_name of this ModelServiceRsp.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ModelServiceRsp.

        模型部署服务的用户名称

        :param user_name: The user_name of this ModelServiceRsp.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def platform(self):
        r"""Gets the platform of this ModelServiceRsp.

        部署平台，Modelarts或者CCE

        :return: The platform of this ModelServiceRsp.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this ModelServiceRsp.

        部署平台，Modelarts或者CCE

        :param platform: The platform of this ModelServiceRsp.
        :type platform: str
        """
        self._platform = platform

    @property
    def train_obs_output(self):
        r"""Gets the train_obs_output of this ModelServiceRsp.

        训练产物OBS地址

        :return: The train_obs_output of this ModelServiceRsp.
        :rtype: str
        """
        return self._train_obs_output

    @train_obs_output.setter
    def train_obs_output(self, train_obs_output):
        r"""Sets the train_obs_output of this ModelServiceRsp.

        训练产物OBS地址

        :param train_obs_output: The train_obs_output of this ModelServiceRsp.
        :type train_obs_output: str
        """
        self._train_obs_output = train_obs_output

    @property
    def use_type(self):
        r"""Gets the use_type of this ModelServiceRsp.

        使用类型，private表示用户创建的服务，public表示预置服务

        :return: The use_type of this ModelServiceRsp.
        :rtype: str
        """
        return self._use_type

    @use_type.setter
    def use_type(self, use_type):
        r"""Sets the use_type of this ModelServiceRsp.

        使用类型，private表示用户创建的服务，public表示预置服务

        :param use_type: The use_type of this ModelServiceRsp.
        :type use_type: str
        """
        self._use_type = use_type

    @property
    def service_config(self):
        r"""Gets the service_config of this ModelServiceRsp.

        :return: The service_config of this ModelServiceRsp.
        :rtype: :class:`huaweicloudsdkoptverse.v1.ModelServiceConfig`
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        r"""Sets the service_config of this ModelServiceRsp.

        :param service_config: The service_config of this ModelServiceRsp.
        :type service_config: :class:`huaweicloudsdkoptverse.v1.ModelServiceConfig`
        """
        self._service_config = service_config

    @property
    def create_time(self):
        r"""Gets the create_time of this ModelServiceRsp.

        创建时间

        :return: The create_time of this ModelServiceRsp.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ModelServiceRsp.

        创建时间

        :param create_time: The create_time of this ModelServiceRsp.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ModelServiceRsp.

        更新时间

        :return: The update_time of this ModelServiceRsp.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ModelServiceRsp.

        更新时间

        :param update_time: The update_time of this ModelServiceRsp.
        :type update_time: int
        """
        self._update_time = update_time

    def to_dict(self):
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
        if not isinstance(other, ModelServiceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
