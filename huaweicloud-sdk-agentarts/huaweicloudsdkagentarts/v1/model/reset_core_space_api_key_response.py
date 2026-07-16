# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetCoreSpaceApiKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'job_name': 'str',
        'status': 'str',
        'key_id': 'str',
        'api_key': 'str'
    }

    attribute_map = {
        'id': 'id',
        'job_name': 'job_name',
        'status': 'status',
        'key_id': 'key_id',
        'api_key': 'api_key'
    }

    def __init__(self, id=None, job_name=None, status=None, key_id=None, api_key=None):
        r"""ResetCoreSpaceApiKeyResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 异步任务 ID，唯一标识一个异步任务，可通过创建异步任务的接口返回获取。 **取值范围：** 不涉及。 
        :type id: str
        :param job_name: **参数解释：** 异步任务名称，标识任务的类型。 **取值范围：** - create_space: 创建记忆库 - update_network: 更新网络配置 
        :type job_name: str
        :param status: **参数解释：** 异步任务的当前执行状态。 **取值范围：** - running: 执行中 - success: 成功 - failed: 失败 
        :type status: str
        :param key_id: **参数解释：** API Key ID（与任务 ID 区分），可通过\&quot;创建 API Key\&quot;接口获取。 **取值范围：** 不涉及。 
        :type key_id: str
        :param api_key: **参数解释：** API Key 明文（仅创建时返回一次，请妥善保存）。 **取值范围：** 不涉及。 
        :type api_key: str
        """
        
        super().__init__()

        self._id = None
        self._job_name = None
        self._status = None
        self._key_id = None
        self._api_key = None
        self.discriminator = None

        self.id = id
        self.job_name = job_name
        self.status = status
        if key_id is not None:
            self.key_id = key_id
        if api_key is not None:
            self.api_key = api_key

    @property
    def id(self):
        r"""Gets the id of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** 异步任务 ID，唯一标识一个异步任务，可通过创建异步任务的接口返回获取。 **取值范围：** 不涉及。 

        :return: The id of this ResetCoreSpaceApiKeyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** 异步任务 ID，唯一标识一个异步任务，可通过创建异步任务的接口返回获取。 **取值范围：** 不涉及。 

        :param id: The id of this ResetCoreSpaceApiKeyResponse.
        :type id: str
        """
        self._id = id

    @property
    def job_name(self):
        r"""Gets the job_name of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** 异步任务名称，标识任务的类型。 **取值范围：** - create_space: 创建记忆库 - update_network: 更新网络配置 

        :return: The job_name of this ResetCoreSpaceApiKeyResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** 异步任务名称，标识任务的类型。 **取值范围：** - create_space: 创建记忆库 - update_network: 更新网络配置 

        :param job_name: The job_name of this ResetCoreSpaceApiKeyResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def status(self):
        r"""Gets the status of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** 异步任务的当前执行状态。 **取值范围：** - running: 执行中 - success: 成功 - failed: 失败 

        :return: The status of this ResetCoreSpaceApiKeyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** 异步任务的当前执行状态。 **取值范围：** - running: 执行中 - success: 成功 - failed: 失败 

        :param status: The status of this ResetCoreSpaceApiKeyResponse.
        :type status: str
        """
        self._status = status

    @property
    def key_id(self):
        r"""Gets the key_id of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** API Key ID（与任务 ID 区分），可通过\"创建 API Key\"接口获取。 **取值范围：** 不涉及。 

        :return: The key_id of this ResetCoreSpaceApiKeyResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** API Key ID（与任务 ID 区分），可通过\"创建 API Key\"接口获取。 **取值范围：** 不涉及。 

        :param key_id: The key_id of this ResetCoreSpaceApiKeyResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def api_key(self):
        r"""Gets the api_key of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** API Key 明文（仅创建时返回一次，请妥善保存）。 **取值范围：** 不涉及。 

        :return: The api_key of this ResetCoreSpaceApiKeyResponse.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this ResetCoreSpaceApiKeyResponse.

        **参数解释：** API Key 明文（仅创建时返回一次，请妥善保存）。 **取值范围：** 不涉及。 

        :param api_key: The api_key of this ResetCoreSpaceApiKeyResponse.
        :type api_key: str
        """
        self._api_key = api_key

    def to_dict(self):
        import warnings
        warnings.warn("ResetCoreSpaceApiKeyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ResetCoreSpaceApiKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
