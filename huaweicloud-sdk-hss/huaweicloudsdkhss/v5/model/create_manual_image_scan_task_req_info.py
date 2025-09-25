# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateManualImageScanTaskReqInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_scope': 'int',
        'rate_limit': 'int',
        'is_all': 'bool',
        'query_info': 'CreateManualImageScanTaskReqInfoQueryInfo',
        'image_info': 'list[CreateManualImageScanTaskReqInfoImageInfo]'
    }

    attribute_map = {
        'scan_scope': 'scan_scope',
        'rate_limit': 'rate_limit',
        'is_all': 'is_all',
        'query_info': 'query_info',
        'image_info': 'image_info'
    }

    def __init__(self, scan_scope=None, rate_limit=None, is_all=None, query_info=None, image_info=None):
        r"""CreateManualImageScanTaskReqInfo

        The model defined in huaweicloud sdk

        :param scan_scope: **参数解释**: 扫描风险类型 **约束限制**: 不涉及 **取值范围**: - 0：none。 - 0x7fffffff：全部。 - 0x000f0000：漏洞。 - 0x0000f000：基线检查。 - 0x00000f00：恶意文件。 - 0x000000f0：敏感信息。 - 0x0000000f：软件合规。  **默认取值**: 不涉及 
        :type scan_scope: int
        :param rate_limit: **参数解释**: 扫描限速 单位：个/h **约束限制**: 不涉及 **取值范围**: 0-1000，0表示不限制。  **默认取值**: 不涉及 
        :type rate_limit: int
        :param is_all: **参数解释**: 扫描全部镜像 **约束限制**: 不涉及 **取值范围**: - true：扫描全部镜像。 - false：指定镜像扫描,见image_info字段。  **默认取值**: 不涉及 
        :type is_all: bool
        :param query_info: 
        :type query_info: :class:`huaweicloudsdkhss.v5.CreateManualImageScanTaskReqInfoQueryInfo`
        :param image_info: 待扫描镜像
        :type image_info: list[:class:`huaweicloudsdkhss.v5.CreateManualImageScanTaskReqInfoImageInfo`]
        """
        
        

        self._scan_scope = None
        self._rate_limit = None
        self._is_all = None
        self._query_info = None
        self._image_info = None
        self.discriminator = None

        if scan_scope is not None:
            self.scan_scope = scan_scope
        if rate_limit is not None:
            self.rate_limit = rate_limit
        if is_all is not None:
            self.is_all = is_all
        if query_info is not None:
            self.query_info = query_info
        if image_info is not None:
            self.image_info = image_info

    @property
    def scan_scope(self):
        r"""Gets the scan_scope of this CreateManualImageScanTaskReqInfo.

        **参数解释**: 扫描风险类型 **约束限制**: 不涉及 **取值范围**: - 0：none。 - 0x7fffffff：全部。 - 0x000f0000：漏洞。 - 0x0000f000：基线检查。 - 0x00000f00：恶意文件。 - 0x000000f0：敏感信息。 - 0x0000000f：软件合规。  **默认取值**: 不涉及 

        :return: The scan_scope of this CreateManualImageScanTaskReqInfo.
        :rtype: int
        """
        return self._scan_scope

    @scan_scope.setter
    def scan_scope(self, scan_scope):
        r"""Sets the scan_scope of this CreateManualImageScanTaskReqInfo.

        **参数解释**: 扫描风险类型 **约束限制**: 不涉及 **取值范围**: - 0：none。 - 0x7fffffff：全部。 - 0x000f0000：漏洞。 - 0x0000f000：基线检查。 - 0x00000f00：恶意文件。 - 0x000000f0：敏感信息。 - 0x0000000f：软件合规。  **默认取值**: 不涉及 

        :param scan_scope: The scan_scope of this CreateManualImageScanTaskReqInfo.
        :type scan_scope: int
        """
        self._scan_scope = scan_scope

    @property
    def rate_limit(self):
        r"""Gets the rate_limit of this CreateManualImageScanTaskReqInfo.

        **参数解释**: 扫描限速 单位：个/h **约束限制**: 不涉及 **取值范围**: 0-1000，0表示不限制。  **默认取值**: 不涉及 

        :return: The rate_limit of this CreateManualImageScanTaskReqInfo.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        r"""Sets the rate_limit of this CreateManualImageScanTaskReqInfo.

        **参数解释**: 扫描限速 单位：个/h **约束限制**: 不涉及 **取值范围**: 0-1000，0表示不限制。  **默认取值**: 不涉及 

        :param rate_limit: The rate_limit of this CreateManualImageScanTaskReqInfo.
        :type rate_limit: int
        """
        self._rate_limit = rate_limit

    @property
    def is_all(self):
        r"""Gets the is_all of this CreateManualImageScanTaskReqInfo.

        **参数解释**: 扫描全部镜像 **约束限制**: 不涉及 **取值范围**: - true：扫描全部镜像。 - false：指定镜像扫描,见image_info字段。  **默认取值**: 不涉及 

        :return: The is_all of this CreateManualImageScanTaskReqInfo.
        :rtype: bool
        """
        return self._is_all

    @is_all.setter
    def is_all(self, is_all):
        r"""Sets the is_all of this CreateManualImageScanTaskReqInfo.

        **参数解释**: 扫描全部镜像 **约束限制**: 不涉及 **取值范围**: - true：扫描全部镜像。 - false：指定镜像扫描,见image_info字段。  **默认取值**: 不涉及 

        :param is_all: The is_all of this CreateManualImageScanTaskReqInfo.
        :type is_all: bool
        """
        self._is_all = is_all

    @property
    def query_info(self):
        r"""Gets the query_info of this CreateManualImageScanTaskReqInfo.

        :return: The query_info of this CreateManualImageScanTaskReqInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.CreateManualImageScanTaskReqInfoQueryInfo`
        """
        return self._query_info

    @query_info.setter
    def query_info(self, query_info):
        r"""Sets the query_info of this CreateManualImageScanTaskReqInfo.

        :param query_info: The query_info of this CreateManualImageScanTaskReqInfo.
        :type query_info: :class:`huaweicloudsdkhss.v5.CreateManualImageScanTaskReqInfoQueryInfo`
        """
        self._query_info = query_info

    @property
    def image_info(self):
        r"""Gets the image_info of this CreateManualImageScanTaskReqInfo.

        待扫描镜像

        :return: The image_info of this CreateManualImageScanTaskReqInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CreateManualImageScanTaskReqInfoImageInfo`]
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        r"""Sets the image_info of this CreateManualImageScanTaskReqInfo.

        待扫描镜像

        :param image_info: The image_info of this CreateManualImageScanTaskReqInfo.
        :type image_info: list[:class:`huaweicloudsdkhss.v5.CreateManualImageScanTaskReqInfoImageInfo`]
        """
        self._image_info = image_info

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
        if not isinstance(other, CreateManualImageScanTaskReqInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
