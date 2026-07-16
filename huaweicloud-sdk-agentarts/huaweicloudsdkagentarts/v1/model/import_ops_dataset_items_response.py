# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportOpsDatasetItemsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'import_task_id': 'str',
        'obs_url': 'str'
    }

    attribute_map = {
        'import_task_id': 'import_task_id',
        'obs_url': 'obs_url'
    }

    def __init__(self, import_task_id=None, obs_url=None):
        r"""ImportOpsDatasetItemsResponse

        The model defined in huaweicloud sdk

        :param import_task_id: **参数解释：** 系统为本次导入操作生成的异步任务唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 
        :type import_task_id: str
        :param obs_url: **参数解释：** 用于将本地数据文件直接上传至对象存储（OBS）的预签名 URL 地址。 **取值范围：** 合法的 HTTP/HTTPS 协议 URL 字符串。 
        :type obs_url: str
        """
        
        super().__init__()

        self._import_task_id = None
        self._obs_url = None
        self.discriminator = None

        if import_task_id is not None:
            self.import_task_id = import_task_id
        if obs_url is not None:
            self.obs_url = obs_url

    @property
    def import_task_id(self):
        r"""Gets the import_task_id of this ImportOpsDatasetItemsResponse.

        **参数解释：** 系统为本次导入操作生成的异步任务唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :return: The import_task_id of this ImportOpsDatasetItemsResponse.
        :rtype: str
        """
        return self._import_task_id

    @import_task_id.setter
    def import_task_id(self, import_task_id):
        r"""Sets the import_task_id of this ImportOpsDatasetItemsResponse.

        **参数解释：** 系统为本次导入操作生成的异步任务唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :param import_task_id: The import_task_id of this ImportOpsDatasetItemsResponse.
        :type import_task_id: str
        """
        self._import_task_id = import_task_id

    @property
    def obs_url(self):
        r"""Gets the obs_url of this ImportOpsDatasetItemsResponse.

        **参数解释：** 用于将本地数据文件直接上传至对象存储（OBS）的预签名 URL 地址。 **取值范围：** 合法的 HTTP/HTTPS 协议 URL 字符串。 

        :return: The obs_url of this ImportOpsDatasetItemsResponse.
        :rtype: str
        """
        return self._obs_url

    @obs_url.setter
    def obs_url(self, obs_url):
        r"""Sets the obs_url of this ImportOpsDatasetItemsResponse.

        **参数解释：** 用于将本地数据文件直接上传至对象存储（OBS）的预签名 URL 地址。 **取值范围：** 合法的 HTTP/HTTPS 协议 URL 字符串。 

        :param obs_url: The obs_url of this ImportOpsDatasetItemsResponse.
        :type obs_url: str
        """
        self._obs_url = obs_url

    def to_dict(self):
        import warnings
        warnings.warn("ImportOpsDatasetItemsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ImportOpsDatasetItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
