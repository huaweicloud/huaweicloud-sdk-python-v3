# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLtsInfoConfigResponse(SdkResponse):

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
        'enabled': 'bool',
        'lts_id_info': 'LtsIdInfo',
        'enabale': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'enabled': 'enabled',
        'lts_id_info': 'ltsIdInfo',
        'enabale': 'enabale'
    }

    def __init__(self, id=None, enabled=None, lts_id_info=None, enabale=None):
        """ShowLtsInfoConfigResponse

        The model defined in huaweicloud sdk

        :param id: lts配置信息id，每个企业项目对应唯一id
        :type id: str
        :param enabled: 是否开启全量日志   - false: 不开启   - true: 开启
        :type enabled: bool
        :param lts_id_info: 
        :type lts_id_info: :class:`huaweicloudsdkwaf.v1.LtsIdInfo`
        :param enabale: 该参数废弃，请忽略
        :type enabale: bool
        """
        
        super(ShowLtsInfoConfigResponse, self).__init__()

        self._id = None
        self._enabled = None
        self._lts_id_info = None
        self._enabale = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if enabled is not None:
            self.enabled = enabled
        if lts_id_info is not None:
            self.lts_id_info = lts_id_info
        if enabale is not None:
            self.enabale = enabale

    @property
    def id(self):
        """Gets the id of this ShowLtsInfoConfigResponse.

        lts配置信息id，每个企业项目对应唯一id

        :return: The id of this ShowLtsInfoConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowLtsInfoConfigResponse.

        lts配置信息id，每个企业项目对应唯一id

        :param id: The id of this ShowLtsInfoConfigResponse.
        :type id: str
        """
        self._id = id

    @property
    def enabled(self):
        """Gets the enabled of this ShowLtsInfoConfigResponse.

        是否开启全量日志   - false: 不开启   - true: 开启

        :return: The enabled of this ShowLtsInfoConfigResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ShowLtsInfoConfigResponse.

        是否开启全量日志   - false: 不开启   - true: 开启

        :param enabled: The enabled of this ShowLtsInfoConfigResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def lts_id_info(self):
        """Gets the lts_id_info of this ShowLtsInfoConfigResponse.

        :return: The lts_id_info of this ShowLtsInfoConfigResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.LtsIdInfo`
        """
        return self._lts_id_info

    @lts_id_info.setter
    def lts_id_info(self, lts_id_info):
        """Sets the lts_id_info of this ShowLtsInfoConfigResponse.

        :param lts_id_info: The lts_id_info of this ShowLtsInfoConfigResponse.
        :type lts_id_info: :class:`huaweicloudsdkwaf.v1.LtsIdInfo`
        """
        self._lts_id_info = lts_id_info

    @property
    def enabale(self):
        """Gets the enabale of this ShowLtsInfoConfigResponse.

        该参数废弃，请忽略

        :return: The enabale of this ShowLtsInfoConfigResponse.
        :rtype: bool
        """
        return self._enabale

    @enabale.setter
    def enabale(self, enabale):
        """Sets the enabale of this ShowLtsInfoConfigResponse.

        该参数废弃，请忽略

        :param enabale: The enabale of this ShowLtsInfoConfigResponse.
        :type enabale: bool
        """
        self._enabale = enabale

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
        if not isinstance(other, ShowLtsInfoConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
