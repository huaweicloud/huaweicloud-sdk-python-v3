# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'csvc': 'str',
        'enable': 'str',
        'is_region': 'int',
        'reference': 'DatasetInfoReference',
        'source_id': 'int',
        'source_name': 'str',
        'target': 'object',
        'type': 'int'
    }

    attribute_map = {
        'csvc': 'csvc',
        'enable': 'enable',
        'is_region': 'is_region',
        'reference': 'reference',
        'source_id': 'source_id',
        'source_name': 'source_name',
        'target': 'target',
        'type': 'type'
    }

    def __init__(self, csvc=None, enable=None, is_region=None, reference=None, source_id=None, source_name=None, target=None, type=None):
        r"""DatasetInfo

        The model defined in huaweicloud sdk

        :param csvc: 所属云服务,例如主机安全就填写hss
        :type csvc: str
        :param enable: 启用状态：0未启用；1启用
        :type enable: str
        :param is_region: 位置信息：1 region；0 global
        :type is_region: int
        :param reference: 
        :type reference: :class:`huaweicloudsdksecmaster.v1.DatasetInfoReference`
        :param source_id: 数据源ID
        :type source_id: int
        :param source_name: 数据源名称
        :type source_name: str
        :param target: 目标管道信息
        :type target: object
        :param type: 订阅类型：1租户订阅；2租户行管订阅；3平台行管(当前都为1)
        :type type: int
        """
        
        

        self._csvc = None
        self._enable = None
        self._is_region = None
        self._reference = None
        self._source_id = None
        self._source_name = None
        self._target = None
        self._type = None
        self.discriminator = None

        self.csvc = csvc
        self.enable = enable
        self.is_region = is_region
        self.reference = reference
        self.source_id = source_id
        self.source_name = source_name
        self.target = target
        self.type = type

    @property
    def csvc(self):
        r"""Gets the csvc of this DatasetInfo.

        所属云服务,例如主机安全就填写hss

        :return: The csvc of this DatasetInfo.
        :rtype: str
        """
        return self._csvc

    @csvc.setter
    def csvc(self, csvc):
        r"""Sets the csvc of this DatasetInfo.

        所属云服务,例如主机安全就填写hss

        :param csvc: The csvc of this DatasetInfo.
        :type csvc: str
        """
        self._csvc = csvc

    @property
    def enable(self):
        r"""Gets the enable of this DatasetInfo.

        启用状态：0未启用；1启用

        :return: The enable of this DatasetInfo.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this DatasetInfo.

        启用状态：0未启用；1启用

        :param enable: The enable of this DatasetInfo.
        :type enable: str
        """
        self._enable = enable

    @property
    def is_region(self):
        r"""Gets the is_region of this DatasetInfo.

        位置信息：1 region；0 global

        :return: The is_region of this DatasetInfo.
        :rtype: int
        """
        return self._is_region

    @is_region.setter
    def is_region(self, is_region):
        r"""Sets the is_region of this DatasetInfo.

        位置信息：1 region；0 global

        :param is_region: The is_region of this DatasetInfo.
        :type is_region: int
        """
        self._is_region = is_region

    @property
    def reference(self):
        r"""Gets the reference of this DatasetInfo.

        :return: The reference of this DatasetInfo.
        :rtype: :class:`huaweicloudsdksecmaster.v1.DatasetInfoReference`
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        r"""Sets the reference of this DatasetInfo.

        :param reference: The reference of this DatasetInfo.
        :type reference: :class:`huaweicloudsdksecmaster.v1.DatasetInfoReference`
        """
        self._reference = reference

    @property
    def source_id(self):
        r"""Gets the source_id of this DatasetInfo.

        数据源ID

        :return: The source_id of this DatasetInfo.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this DatasetInfo.

        数据源ID

        :param source_id: The source_id of this DatasetInfo.
        :type source_id: int
        """
        self._source_id = source_id

    @property
    def source_name(self):
        r"""Gets the source_name of this DatasetInfo.

        数据源名称

        :return: The source_name of this DatasetInfo.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this DatasetInfo.

        数据源名称

        :param source_name: The source_name of this DatasetInfo.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def target(self):
        r"""Gets the target of this DatasetInfo.

        目标管道信息

        :return: The target of this DatasetInfo.
        :rtype: object
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this DatasetInfo.

        目标管道信息

        :param target: The target of this DatasetInfo.
        :type target: object
        """
        self._target = target

    @property
    def type(self):
        r"""Gets the type of this DatasetInfo.

        订阅类型：1租户订阅；2租户行管订阅；3平台行管(当前都为1)

        :return: The type of this DatasetInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DatasetInfo.

        订阅类型：1租户订阅；2租户行管订阅；3平台行管(当前都为1)

        :param type: The type of this DatasetInfo.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, DatasetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
