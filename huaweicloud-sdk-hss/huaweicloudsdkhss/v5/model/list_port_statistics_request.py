# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'category': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int',
        'port': 'int',
        'port_string': 'str',
        'type': 'str',
        'status': 'str',
        'sort_key': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'category': 'category',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset',
        'port': 'port',
        'port_string': 'port_string',
        'type': 'type',
        'status': 'status',
        'sort_key': 'sort_key'
    }

    def __init__(self, enterprise_project_id=None, category=None, sort_dir=None, limit=None, offset=None, port=None, port_string=None, type=None, status=None, sort_key=None):
        r"""ListPortStatisticsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param category: **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host：主机 - container：容器  **默认取值**: 不涉及 
        :type category: str
        :param sort_dir: **参数解释**: 排序的顺序 **约束限制**: 不涉及 **取值范围**:   - asc  : 正序   - desc : 倒序  **默认取值**: 正序排序 
        :type sort_dir: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param port: **参数解释**: 端口号，该字段用来进行精确匹配 **约束限制**: 与port_string同时使用的话，二者有包含关系则按精确匹配，无包含关系则结果为空 **取值范围**: 最小值1，最大值65535 **默认取值**: 不涉及 
        :type port: int
        :param port_string: **参数解释**: 端口字符串，该字段用来进行模糊匹配 **约束限制**: 与port同时使用的话，二者有包含关系则按精确匹配，无包含关系则结果为空 **取值范围**: 最小值1，最大值65535 **默认取值**: 不涉及 
        :type port_string: str
        :param type: **参数解释**: 端口类型 **约束限制**: 不涉及 **取值范围**: - UDP - UDP6 - TCP - TCP6  **默认取值**: 不涉及 
        :type type: str
        :param status: **参数解释**: 端口状态 **约束限制**: 不涉及 **取值范围**: - danger: 危险端口 - normal: 正常端口 - unknow: 无已知危险的端口  **默认取值**: 不涉及 
        :type status: str
        :param sort_key: **参数解释**: 排序的key值，目前支持按照端口号port排序 **约束限制**: 不涉及 **取值范围**: - port: 端口号  **默认取值**: 不涉及 
        :type sort_key: str
        """
        
        

        self._enterprise_project_id = None
        self._category = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self._port = None
        self._port_string = None
        self._type = None
        self._status = None
        self._sort_key = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if category is not None:
            self.category = category
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if port is not None:
            self.port = port
        if port_string is not None:
            self.port_string = port_string
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if sort_key is not None:
            self.sort_key = sort_key

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPortStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPortStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListPortStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def category(self):
        r"""Gets the category of this ListPortStatisticsRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host：主机 - container：容器  **默认取值**: 不涉及 

        :return: The category of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListPortStatisticsRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host：主机 - container：容器  **默认取值**: 不涉及 

        :param category: The category of this ListPortStatisticsRequest.
        :type category: str
        """
        self._category = category

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListPortStatisticsRequest.

        **参数解释**: 排序的顺序 **约束限制**: 不涉及 **取值范围**:   - asc  : 正序   - desc : 倒序  **默认取值**: 正序排序 

        :return: The sort_dir of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListPortStatisticsRequest.

        **参数解释**: 排序的顺序 **约束限制**: 不涉及 **取值范围**:   - asc  : 正序   - desc : 倒序  **默认取值**: 正序排序 

        :param sort_dir: The sort_dir of this ListPortStatisticsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListPortStatisticsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListPortStatisticsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPortStatisticsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListPortStatisticsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPortStatisticsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListPortStatisticsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPortStatisticsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListPortStatisticsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def port(self):
        r"""Gets the port of this ListPortStatisticsRequest.

        **参数解释**: 端口号，该字段用来进行精确匹配 **约束限制**: 与port_string同时使用的话，二者有包含关系则按精确匹配，无包含关系则结果为空 **取值范围**: 最小值1，最大值65535 **默认取值**: 不涉及 

        :return: The port of this ListPortStatisticsRequest.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ListPortStatisticsRequest.

        **参数解释**: 端口号，该字段用来进行精确匹配 **约束限制**: 与port_string同时使用的话，二者有包含关系则按精确匹配，无包含关系则结果为空 **取值范围**: 最小值1，最大值65535 **默认取值**: 不涉及 

        :param port: The port of this ListPortStatisticsRequest.
        :type port: int
        """
        self._port = port

    @property
    def port_string(self):
        r"""Gets the port_string of this ListPortStatisticsRequest.

        **参数解释**: 端口字符串，该字段用来进行模糊匹配 **约束限制**: 与port同时使用的话，二者有包含关系则按精确匹配，无包含关系则结果为空 **取值范围**: 最小值1，最大值65535 **默认取值**: 不涉及 

        :return: The port_string of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._port_string

    @port_string.setter
    def port_string(self, port_string):
        r"""Sets the port_string of this ListPortStatisticsRequest.

        **参数解释**: 端口字符串，该字段用来进行模糊匹配 **约束限制**: 与port同时使用的话，二者有包含关系则按精确匹配，无包含关系则结果为空 **取值范围**: 最小值1，最大值65535 **默认取值**: 不涉及 

        :param port_string: The port_string of this ListPortStatisticsRequest.
        :type port_string: str
        """
        self._port_string = port_string

    @property
    def type(self):
        r"""Gets the type of this ListPortStatisticsRequest.

        **参数解释**: 端口类型 **约束限制**: 不涉及 **取值范围**: - UDP - UDP6 - TCP - TCP6  **默认取值**: 不涉及 

        :return: The type of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListPortStatisticsRequest.

        **参数解释**: 端口类型 **约束限制**: 不涉及 **取值范围**: - UDP - UDP6 - TCP - TCP6  **默认取值**: 不涉及 

        :param type: The type of this ListPortStatisticsRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ListPortStatisticsRequest.

        **参数解释**: 端口状态 **约束限制**: 不涉及 **取值范围**: - danger: 危险端口 - normal: 正常端口 - unknow: 无已知危险的端口  **默认取值**: 不涉及 

        :return: The status of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPortStatisticsRequest.

        **参数解释**: 端口状态 **约束限制**: 不涉及 **取值范围**: - danger: 危险端口 - normal: 正常端口 - unknow: 无已知危险的端口  **默认取值**: 不涉及 

        :param status: The status of this ListPortStatisticsRequest.
        :type status: str
        """
        self._status = status

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListPortStatisticsRequest.

        **参数解释**: 排序的key值，目前支持按照端口号port排序 **约束限制**: 不涉及 **取值范围**: - port: 端口号  **默认取值**: 不涉及 

        :return: The sort_key of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListPortStatisticsRequest.

        **参数解释**: 排序的key值，目前支持按照端口号port排序 **约束限制**: 不涉及 **取值范围**: - port: 端口号  **默认取值**: 不涉及 

        :param sort_key: The sort_key of this ListPortStatisticsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

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
        if not isinstance(other, ListPortStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
