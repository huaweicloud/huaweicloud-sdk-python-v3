# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowModelServiceListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'infer_type': 'str',
        'asset_id': 'str',
        'asset_type': 'str',
        'asset_sub_type': 'str',
        'chip_type': 'str',
        'platform': 'str',
        'status': 'str',
        'use_type': 'str',
        'model_name': 'str',
        'service_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_dir': 'str'
    }

    attribute_map = {
        'infer_type': 'infer_type',
        'asset_id': 'asset_id',
        'asset_type': 'asset_type',
        'asset_sub_type': 'asset_sub_type',
        'chip_type': 'chip_type',
        'platform': 'platform',
        'status': 'status',
        'use_type': 'use_type',
        'model_name': 'model_name',
        'service_name': 'service_name',
        'offset': 'offset',
        'limit': 'limit',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, infer_type=None, asset_id=None, asset_type=None, asset_sub_type=None, chip_type=None, platform=None, status=None, use_type=None, model_name=None, service_name=None, offset=None, limit=None, sort_dir=None):
        r"""ShowModelServiceListRequest

        The model defined in huaweicloud sdk

        :param infer_type: 推理类型，分为online和edge
        :type infer_type: str
        :param asset_id: 推理服务所关联的模型ID
        :type asset_id: str
        :param asset_type: 推理服务所关联的模型类型
        :type asset_type: str
        :param asset_sub_type: 推理服务所关联的模型子类型
        :type asset_sub_type: str
        :param chip_type: 芯片类型
        :type chip_type: str
        :param platform: 部署平台，Modelarts或者CCE
        :type platform: str
        :param status: 服务状态，INIT/DEPLOYING/RUNNING/SUCCEEDED/FAILED/STOPPED/PENDING/CANCELLED/WAITING
        :type status: str
        :param use_type: 使用类型，private表示用户创建的服务，public表示预置服务
        :type use_type: str
        :param model_name: 模型名称，支持模糊匹配
        :type model_name: str
        :param service_name: 服务名称，支持模糊匹配
        :type service_name: str
        :param offset: 偏移量，取值范围[0,100000000]，默认值0
        :type offset: int
        :param limit: 返回限制个数，取值范围[1-1000]，默认值100
        :type limit: int
        :param sort_dir: **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 
        :type sort_dir: str
        """
        
        

        self._infer_type = None
        self._asset_id = None
        self._asset_type = None
        self._asset_sub_type = None
        self._chip_type = None
        self._platform = None
        self._status = None
        self._use_type = None
        self._model_name = None
        self._service_name = None
        self._offset = None
        self._limit = None
        self._sort_dir = None
        self.discriminator = None

        if infer_type is not None:
            self.infer_type = infer_type
        if asset_id is not None:
            self.asset_id = asset_id
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_sub_type is not None:
            self.asset_sub_type = asset_sub_type
        if chip_type is not None:
            self.chip_type = chip_type
        if platform is not None:
            self.platform = platform
        if status is not None:
            self.status = status
        if use_type is not None:
            self.use_type = use_type
        if model_name is not None:
            self.model_name = model_name
        if service_name is not None:
            self.service_name = service_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def infer_type(self):
        r"""Gets the infer_type of this ShowModelServiceListRequest.

        推理类型，分为online和edge

        :return: The infer_type of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._infer_type

    @infer_type.setter
    def infer_type(self, infer_type):
        r"""Sets the infer_type of this ShowModelServiceListRequest.

        推理类型，分为online和edge

        :param infer_type: The infer_type of this ShowModelServiceListRequest.
        :type infer_type: str
        """
        self._infer_type = infer_type

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ShowModelServiceListRequest.

        推理服务所关联的模型ID

        :return: The asset_id of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ShowModelServiceListRequest.

        推理服务所关联的模型ID

        :param asset_id: The asset_id of this ShowModelServiceListRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ShowModelServiceListRequest.

        推理服务所关联的模型类型

        :return: The asset_type of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ShowModelServiceListRequest.

        推理服务所关联的模型类型

        :param asset_type: The asset_type of this ShowModelServiceListRequest.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_sub_type(self):
        r"""Gets the asset_sub_type of this ShowModelServiceListRequest.

        推理服务所关联的模型子类型

        :return: The asset_sub_type of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._asset_sub_type

    @asset_sub_type.setter
    def asset_sub_type(self, asset_sub_type):
        r"""Sets the asset_sub_type of this ShowModelServiceListRequest.

        推理服务所关联的模型子类型

        :param asset_sub_type: The asset_sub_type of this ShowModelServiceListRequest.
        :type asset_sub_type: str
        """
        self._asset_sub_type = asset_sub_type

    @property
    def chip_type(self):
        r"""Gets the chip_type of this ShowModelServiceListRequest.

        芯片类型

        :return: The chip_type of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._chip_type

    @chip_type.setter
    def chip_type(self, chip_type):
        r"""Sets the chip_type of this ShowModelServiceListRequest.

        芯片类型

        :param chip_type: The chip_type of this ShowModelServiceListRequest.
        :type chip_type: str
        """
        self._chip_type = chip_type

    @property
    def platform(self):
        r"""Gets the platform of this ShowModelServiceListRequest.

        部署平台，Modelarts或者CCE

        :return: The platform of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this ShowModelServiceListRequest.

        部署平台，Modelarts或者CCE

        :param platform: The platform of this ShowModelServiceListRequest.
        :type platform: str
        """
        self._platform = platform

    @property
    def status(self):
        r"""Gets the status of this ShowModelServiceListRequest.

        服务状态，INIT/DEPLOYING/RUNNING/SUCCEEDED/FAILED/STOPPED/PENDING/CANCELLED/WAITING

        :return: The status of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowModelServiceListRequest.

        服务状态，INIT/DEPLOYING/RUNNING/SUCCEEDED/FAILED/STOPPED/PENDING/CANCELLED/WAITING

        :param status: The status of this ShowModelServiceListRequest.
        :type status: str
        """
        self._status = status

    @property
    def use_type(self):
        r"""Gets the use_type of this ShowModelServiceListRequest.

        使用类型，private表示用户创建的服务，public表示预置服务

        :return: The use_type of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._use_type

    @use_type.setter
    def use_type(self, use_type):
        r"""Sets the use_type of this ShowModelServiceListRequest.

        使用类型，private表示用户创建的服务，public表示预置服务

        :param use_type: The use_type of this ShowModelServiceListRequest.
        :type use_type: str
        """
        self._use_type = use_type

    @property
    def model_name(self):
        r"""Gets the model_name of this ShowModelServiceListRequest.

        模型名称，支持模糊匹配

        :return: The model_name of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this ShowModelServiceListRequest.

        模型名称，支持模糊匹配

        :param model_name: The model_name of this ShowModelServiceListRequest.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def service_name(self):
        r"""Gets the service_name of this ShowModelServiceListRequest.

        服务名称，支持模糊匹配

        :return: The service_name of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ShowModelServiceListRequest.

        服务名称，支持模糊匹配

        :param service_name: The service_name of this ShowModelServiceListRequest.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def offset(self):
        r"""Gets the offset of this ShowModelServiceListRequest.

        偏移量，取值范围[0,100000000]，默认值0

        :return: The offset of this ShowModelServiceListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowModelServiceListRequest.

        偏移量，取值范围[0,100000000]，默认值0

        :param offset: The offset of this ShowModelServiceListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowModelServiceListRequest.

        返回限制个数，取值范围[1-1000]，默认值100

        :return: The limit of this ShowModelServiceListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowModelServiceListRequest.

        返回限制个数，取值范围[1-1000]，默认值100

        :param limit: The limit of this ShowModelServiceListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ShowModelServiceListRequest.

        **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 

        :return: The sort_dir of this ShowModelServiceListRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ShowModelServiceListRequest.

        **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 

        :param sort_dir: The sort_dir of this ShowModelServiceListRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ShowModelServiceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
