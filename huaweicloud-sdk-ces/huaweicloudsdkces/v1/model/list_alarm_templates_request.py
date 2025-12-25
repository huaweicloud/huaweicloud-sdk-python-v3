# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_template_id': 'str',
        'namespace': 'str',
        'dname': 'str',
        'start': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'alarm_template_id': 'alarmTemplateId',
        'namespace': 'namespace',
        'dname': 'dname',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, alarm_template_id=None, namespace=None, dname=None, start=None, limit=None):
        r"""ListAlarmTemplatesRequest

        The model defined in huaweicloud sdk

        :param alarm_template_id: **参数解释**： 自定义告警模版的ID，如：at1603330892378wkDm77y6B **约束限制**： 不涉及 **取值范围**： 以at开头，后跟字母、数字，长度最长为64 **默认取值**： 不涉及 
        :type alarm_template_id: str
        :param namespace: **参数解释**： 自定义告警模板选择的资源类型。即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及 
        :type namespace: str
        :param dname: **参数解释**： 自定义告警模板选择的资源维度，如：弹性云服务器，则维度为instance_id，各资源的指标维度名称可查看：“[服务指标维度](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 包含0-9/a-z/A-Z/_。字符串的长度必须在 1 到 131个字符之间。 **默认取值**： 不涉及 
        :type dname: str
        :param start: **参数解释**： 分页起始位置，值为告警模版的ID，如：at1603330892378wkDm77y6B。 **约束限制**： 不涉及 **取值范围**： 以at开头，后跟字母、数字，长度最长为64 **默认取值**： 不涉及 
        :type start: str
        :param limit: **参数解释**： 单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。 **约束限制**： 不涉及 **取值范围**： 整数，最小值为1，最大值为100。 **默认取值**： 不涉及 
        :type limit: str
        """
        
        

        self._alarm_template_id = None
        self._namespace = None
        self._dname = None
        self._start = None
        self._limit = None
        self.discriminator = None

        if alarm_template_id is not None:
            self.alarm_template_id = alarm_template_id
        if namespace is not None:
            self.namespace = namespace
        if dname is not None:
            self.dname = dname
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def alarm_template_id(self):
        r"""Gets the alarm_template_id of this ListAlarmTemplatesRequest.

        **参数解释**： 自定义告警模版的ID，如：at1603330892378wkDm77y6B **约束限制**： 不涉及 **取值范围**： 以at开头，后跟字母、数字，长度最长为64 **默认取值**： 不涉及 

        :return: The alarm_template_id of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._alarm_template_id

    @alarm_template_id.setter
    def alarm_template_id(self, alarm_template_id):
        r"""Sets the alarm_template_id of this ListAlarmTemplatesRequest.

        **参数解释**： 自定义告警模版的ID，如：at1603330892378wkDm77y6B **约束限制**： 不涉及 **取值范围**： 以at开头，后跟字母、数字，长度最长为64 **默认取值**： 不涉及 

        :param alarm_template_id: The alarm_template_id of this ListAlarmTemplatesRequest.
        :type alarm_template_id: str
        """
        self._alarm_template_id = alarm_template_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ListAlarmTemplatesRequest.

        **参数解释**： 自定义告警模板选择的资源类型。即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及 

        :return: The namespace of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListAlarmTemplatesRequest.

        **参数解释**： 自定义告警模板选择的资源类型。即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及 

        :param namespace: The namespace of this ListAlarmTemplatesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dname(self):
        r"""Gets the dname of this ListAlarmTemplatesRequest.

        **参数解释**： 自定义告警模板选择的资源维度，如：弹性云服务器，则维度为instance_id，各资源的指标维度名称可查看：“[服务指标维度](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 包含0-9/a-z/A-Z/_。字符串的长度必须在 1 到 131个字符之间。 **默认取值**： 不涉及 

        :return: The dname of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._dname

    @dname.setter
    def dname(self, dname):
        r"""Sets the dname of this ListAlarmTemplatesRequest.

        **参数解释**： 自定义告警模板选择的资源维度，如：弹性云服务器，则维度为instance_id，各资源的指标维度名称可查看：“[服务指标维度](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 包含0-9/a-z/A-Z/_。字符串的长度必须在 1 到 131个字符之间。 **默认取值**： 不涉及 

        :param dname: The dname of this ListAlarmTemplatesRequest.
        :type dname: str
        """
        self._dname = dname

    @property
    def start(self):
        r"""Gets the start of this ListAlarmTemplatesRequest.

        **参数解释**： 分页起始位置，值为告警模版的ID，如：at1603330892378wkDm77y6B。 **约束限制**： 不涉及 **取值范围**： 以at开头，后跟字母、数字，长度最长为64 **默认取值**： 不涉及 

        :return: The start of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListAlarmTemplatesRequest.

        **参数解释**： 分页起始位置，值为告警模版的ID，如：at1603330892378wkDm77y6B。 **约束限制**： 不涉及 **取值范围**： 以at开头，后跟字母、数字，长度最长为64 **默认取值**： 不涉及 

        :param start: The start of this ListAlarmTemplatesRequest.
        :type start: str
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmTemplatesRequest.

        **参数解释**： 单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。 **约束限制**： 不涉及 **取值范围**： 整数，最小值为1，最大值为100。 **默认取值**： 不涉及 

        :return: The limit of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmTemplatesRequest.

        **参数解释**： 单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。 **约束限制**： 不涉及 **取值范围**： 整数，最小值为1，最大值为100。 **默认取值**： 不涉及 

        :param limit: The limit of this ListAlarmTemplatesRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListAlarmTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
