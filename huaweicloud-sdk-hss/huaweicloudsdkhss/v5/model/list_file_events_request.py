# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFileEventsRequest:

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
        'host_name': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'file_name': 'str',
        'file_path': 'str',
        'change_type': 'str',
        'change_category': 'str',
        'status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_name': 'host_name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'file_name': 'file_name',
        'file_path': 'file_path',
        'change_type': 'change_type',
        'change_category': 'change_category',
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, enterprise_project_id=None, host_name=None, begin_time=None, end_time=None, file_name=None, file_path=None, change_type=None, change_category=None, status=None, offset=None, limit=None):
        r"""ListFileEventsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param begin_time: **参数解释**: 开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type begin_time: int
        :param end_time: **参数解释**: 结束时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type end_time: int
        :param file_name: 文件名称
        :type file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param change_type: 变更类型，包含如下:   - \&quot;all\&quot; : 全部   - \&quot;registry\&quot; : 注册表   - \&quot;file\&quot; : 文件
        :type change_type: str
        :param change_category: 变更类别，包含如下:   - \&quot;all\&quot; : 全部   - \&quot;modify\&quot; : 修改   - \&quot;add\&quot; : 新增   - \&quot;delete\&quot; : 删除
        :type change_category: str
        :param status: 状态，包含如下:   - \&quot;all\&quot; : 全部   - \&quot;trust\&quot; : 可信   - \&quot;untrust\&quot; : 不可信   - \&quot;unknown\&quot; : 未知 
        :type status: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        """
        
        

        self._enterprise_project_id = None
        self._host_name = None
        self._begin_time = None
        self._end_time = None
        self._file_name = None
        self._file_path = None
        self._change_type = None
        self._change_category = None
        self._status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_name is not None:
            self.host_name = host_name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if change_type is not None:
            self.change_type = change_type
        if change_category is not None:
            self.change_category = change_category
        if status is not None:
            self.status = status
        self.offset = offset
        self.limit = limit

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListFileEventsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListFileEventsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListFileEventsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListFileEventsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListFileEventsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListFileEventsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListFileEventsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListFileEventsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListFileEventsRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The begin_time of this ListFileEventsRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListFileEventsRequest.

        **参数解释**: 开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param begin_time: The begin_time of this ListFileEventsRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListFileEventsRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The end_time of this ListFileEventsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListFileEventsRequest.

        **参数解释**: 结束时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param end_time: The end_time of this ListFileEventsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def file_name(self):
        r"""Gets the file_name of this ListFileEventsRequest.

        文件名称

        :return: The file_name of this ListFileEventsRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListFileEventsRequest.

        文件名称

        :param file_name: The file_name of this ListFileEventsRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this ListFileEventsRequest.

        文件路径

        :return: The file_path of this ListFileEventsRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ListFileEventsRequest.

        文件路径

        :param file_path: The file_path of this ListFileEventsRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def change_type(self):
        r"""Gets the change_type of this ListFileEventsRequest.

        变更类型，包含如下:   - \"all\" : 全部   - \"registry\" : 注册表   - \"file\" : 文件

        :return: The change_type of this ListFileEventsRequest.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this ListFileEventsRequest.

        变更类型，包含如下:   - \"all\" : 全部   - \"registry\" : 注册表   - \"file\" : 文件

        :param change_type: The change_type of this ListFileEventsRequest.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def change_category(self):
        r"""Gets the change_category of this ListFileEventsRequest.

        变更类别，包含如下:   - \"all\" : 全部   - \"modify\" : 修改   - \"add\" : 新增   - \"delete\" : 删除

        :return: The change_category of this ListFileEventsRequest.
        :rtype: str
        """
        return self._change_category

    @change_category.setter
    def change_category(self, change_category):
        r"""Sets the change_category of this ListFileEventsRequest.

        变更类别，包含如下:   - \"all\" : 全部   - \"modify\" : 修改   - \"add\" : 新增   - \"delete\" : 删除

        :param change_category: The change_category of this ListFileEventsRequest.
        :type change_category: str
        """
        self._change_category = change_category

    @property
    def status(self):
        r"""Gets the status of this ListFileEventsRequest.

        状态，包含如下:   - \"all\" : 全部   - \"trust\" : 可信   - \"untrust\" : 不可信   - \"unknown\" : 未知 

        :return: The status of this ListFileEventsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFileEventsRequest.

        状态，包含如下:   - \"all\" : 全部   - \"trust\" : 可信   - \"untrust\" : 不可信   - \"unknown\" : 未知 

        :param status: The status of this ListFileEventsRequest.
        :type status: str
        """
        self._status = status

    @property
    def offset(self):
        r"""Gets the offset of this ListFileEventsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListFileEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFileEventsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListFileEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFileEventsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListFileEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFileEventsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListFileEventsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListFileEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
