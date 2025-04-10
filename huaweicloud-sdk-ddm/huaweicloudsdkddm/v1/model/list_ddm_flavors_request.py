# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDdmFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'engine_id': 'str',
        'engine_version': 'str',
        'available_zones': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'engine_id': 'engine_id',
        'engine_version': 'engine_version',
        'available_zones': 'available_zones'
    }

    def __init__(self, offset=None, limit=None, engine_id=None, engine_version=None, available_zones=None):
        r"""ListDdmFlavorsRequest

        The model defined in huaweicloud sdk

        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。取值范围：1~128。不传该参数时，默认值为10。
        :type limit: int
        :param engine_id: 引擎ID,通过查询DDM引擎信息接口获取，引擎ID与引擎版本至少指定一个
        :type engine_id: str
        :param engine_version: 引擎版本,通过查询DDM引擎信息接口获取，引擎ID与引擎版本至少指定一个
        :type engine_version: str
        :param available_zones: 可用区，多个用\&quot;,\&quot;分割，如cn-southwest-244a,cn-southwest-244b。请参见地区和终端节点(https://console.huaweicloud.com/apiexplorer/#/endpoint/DDM)。
        :type available_zones: str
        """
        
        

        self._offset = None
        self._limit = None
        self._engine_id = None
        self._engine_version = None
        self._available_zones = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if engine_id is not None:
            self.engine_id = engine_id
        if engine_version is not None:
            self.engine_version = engine_version
        if available_zones is not None:
            self.available_zones = available_zones

    @property
    def offset(self):
        r"""Gets the offset of this ListDdmFlavorsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。

        :return: The offset of this ListDdmFlavorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDdmFlavorsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。

        :param offset: The offset of this ListDdmFlavorsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDdmFlavorsRequest.

        查询个数上限值。取值范围：1~128。不传该参数时，默认值为10。

        :return: The limit of this ListDdmFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDdmFlavorsRequest.

        查询个数上限值。取值范围：1~128。不传该参数时，默认值为10。

        :param limit: The limit of this ListDdmFlavorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def engine_id(self):
        r"""Gets the engine_id of this ListDdmFlavorsRequest.

        引擎ID,通过查询DDM引擎信息接口获取，引擎ID与引擎版本至少指定一个

        :return: The engine_id of this ListDdmFlavorsRequest.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this ListDdmFlavorsRequest.

        引擎ID,通过查询DDM引擎信息接口获取，引擎ID与引擎版本至少指定一个

        :param engine_id: The engine_id of this ListDdmFlavorsRequest.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ListDdmFlavorsRequest.

        引擎版本,通过查询DDM引擎信息接口获取，引擎ID与引擎版本至少指定一个

        :return: The engine_version of this ListDdmFlavorsRequest.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ListDdmFlavorsRequest.

        引擎版本,通过查询DDM引擎信息接口获取，引擎ID与引擎版本至少指定一个

        :param engine_version: The engine_version of this ListDdmFlavorsRequest.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ListDdmFlavorsRequest.

        可用区，多个用\",\"分割，如cn-southwest-244a,cn-southwest-244b。请参见地区和终端节点(https://console.huaweicloud.com/apiexplorer/#/endpoint/DDM)。

        :return: The available_zones of this ListDdmFlavorsRequest.
        :rtype: str
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ListDdmFlavorsRequest.

        可用区，多个用\",\"分割，如cn-southwest-244a,cn-southwest-244b。请参见地区和终端节点(https://console.huaweicloud.com/apiexplorer/#/endpoint/DDM)。

        :param available_zones: The available_zones of this ListDdmFlavorsRequest.
        :type available_zones: str
        """
        self._available_zones = available_zones

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
        if not isinstance(other, ListDdmFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
