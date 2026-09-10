# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelServiceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'request_mode': 'str',
        'description': 'str',
        'platform': 'Platform',
        'train_obs_output': 'str',
        'asset_id': 'str',
        'chat_id': 'str',
        'infer_type': 'InferType',
        'service_config': 'ModelServiceConfig'
    }

    attribute_map = {
        'name': 'name',
        'request_mode': 'request_mode',
        'description': 'description',
        'platform': 'platform',
        'train_obs_output': 'train_obs_output',
        'asset_id': 'asset_id',
        'chat_id': 'chat_id',
        'infer_type': 'infer_type',
        'service_config': 'service_config'
    }

    def __init__(self, name=None, request_mode=None, description=None, platform=None, train_obs_output=None, asset_id=None, chat_id=None, infer_type=None, service_config=None):
        r"""CreateModelServiceReq

        The model defined in huaweicloud sdk

        :param name: 部署名称
        :type name: str
        :param request_mode: 推理类型
        :type request_mode: str
        :param description: 描述
        :type description: str
        :param platform: 
        :type platform: :class:`huaweicloudsdkoptverse.v1.Platform`
        :param train_obs_output: 训练产物OBS地址
        :type train_obs_output: str
        :param asset_id: 资产ID
        :type asset_id: str
        :param chat_id: 对话ID
        :type chat_id: str
        :param infer_type: 
        :type infer_type: :class:`huaweicloudsdkoptverse.v1.InferType`
        :param service_config: 
        :type service_config: :class:`huaweicloudsdkoptverse.v1.ModelServiceConfig`
        """
        
        

        self._name = None
        self._request_mode = None
        self._description = None
        self._platform = None
        self._train_obs_output = None
        self._asset_id = None
        self._chat_id = None
        self._infer_type = None
        self._service_config = None
        self.discriminator = None

        self.name = name
        self.request_mode = request_mode
        if description is not None:
            self.description = description
        self.platform = platform
        if train_obs_output is not None:
            self.train_obs_output = train_obs_output
        self.asset_id = asset_id
        if chat_id is not None:
            self.chat_id = chat_id
        self.infer_type = infer_type
        self.service_config = service_config

    @property
    def name(self):
        r"""Gets the name of this CreateModelServiceReq.

        部署名称

        :return: The name of this CreateModelServiceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModelServiceReq.

        部署名称

        :param name: The name of this CreateModelServiceReq.
        :type name: str
        """
        self._name = name

    @property
    def request_mode(self):
        r"""Gets the request_mode of this CreateModelServiceReq.

        推理类型

        :return: The request_mode of this CreateModelServiceReq.
        :rtype: str
        """
        return self._request_mode

    @request_mode.setter
    def request_mode(self, request_mode):
        r"""Sets the request_mode of this CreateModelServiceReq.

        推理类型

        :param request_mode: The request_mode of this CreateModelServiceReq.
        :type request_mode: str
        """
        self._request_mode = request_mode

    @property
    def description(self):
        r"""Gets the description of this CreateModelServiceReq.

        描述

        :return: The description of this CreateModelServiceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateModelServiceReq.

        描述

        :param description: The description of this CreateModelServiceReq.
        :type description: str
        """
        self._description = description

    @property
    def platform(self):
        r"""Gets the platform of this CreateModelServiceReq.

        :return: The platform of this CreateModelServiceReq.
        :rtype: :class:`huaweicloudsdkoptverse.v1.Platform`
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this CreateModelServiceReq.

        :param platform: The platform of this CreateModelServiceReq.
        :type platform: :class:`huaweicloudsdkoptverse.v1.Platform`
        """
        self._platform = platform

    @property
    def train_obs_output(self):
        r"""Gets the train_obs_output of this CreateModelServiceReq.

        训练产物OBS地址

        :return: The train_obs_output of this CreateModelServiceReq.
        :rtype: str
        """
        return self._train_obs_output

    @train_obs_output.setter
    def train_obs_output(self, train_obs_output):
        r"""Sets the train_obs_output of this CreateModelServiceReq.

        训练产物OBS地址

        :param train_obs_output: The train_obs_output of this CreateModelServiceReq.
        :type train_obs_output: str
        """
        self._train_obs_output = train_obs_output

    @property
    def asset_id(self):
        r"""Gets the asset_id of this CreateModelServiceReq.

        资产ID

        :return: The asset_id of this CreateModelServiceReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this CreateModelServiceReq.

        资产ID

        :param asset_id: The asset_id of this CreateModelServiceReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def chat_id(self):
        r"""Gets the chat_id of this CreateModelServiceReq.

        对话ID

        :return: The chat_id of this CreateModelServiceReq.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        r"""Sets the chat_id of this CreateModelServiceReq.

        对话ID

        :param chat_id: The chat_id of this CreateModelServiceReq.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def infer_type(self):
        r"""Gets the infer_type of this CreateModelServiceReq.

        :return: The infer_type of this CreateModelServiceReq.
        :rtype: :class:`huaweicloudsdkoptverse.v1.InferType`
        """
        return self._infer_type

    @infer_type.setter
    def infer_type(self, infer_type):
        r"""Sets the infer_type of this CreateModelServiceReq.

        :param infer_type: The infer_type of this CreateModelServiceReq.
        :type infer_type: :class:`huaweicloudsdkoptverse.v1.InferType`
        """
        self._infer_type = infer_type

    @property
    def service_config(self):
        r"""Gets the service_config of this CreateModelServiceReq.

        :return: The service_config of this CreateModelServiceReq.
        :rtype: :class:`huaweicloudsdkoptverse.v1.ModelServiceConfig`
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        r"""Sets the service_config of this CreateModelServiceReq.

        :param service_config: The service_config of this CreateModelServiceReq.
        :type service_config: :class:`huaweicloudsdkoptverse.v1.ModelServiceConfig`
        """
        self._service_config = service_config

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
        if not isinstance(other, CreateModelServiceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
