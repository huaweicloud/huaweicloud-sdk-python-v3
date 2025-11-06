# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryAlarmRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'name': 'str',
        'remind_type': 'int',
        'ding_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'name': 'name',
        'remind_type': 'remind_type',
        'ding_name': 'ding_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, workspace=None, x_project_id=None, name=None, remind_type=None, ding_name=None, offset=None, limit=None):
        r"""ListFactoryAlarmRulesRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param name: 作业/规则名称。
        :type name: str
        :param remind_type: 通知类型：  - 0：运行成功。 - 1：运行异常/失败。 - 3：未完成。 - 4：资源繁忙。 - 5：基线任务异常。 - 6：基线预警。 - 7：基线破线。 - 8：基线加剧。 - 9：保障作业预警时间未完成。 - 10：保障作业承诺时间未完成。 - 11：保障作业失败。 - 12：周期未完成。 - 13：运行取消。 - 14：失败作业重跑成功。 - 15：作业改动。 默认查询所有状态。
        :type remind_type: int
        :param ding_name: 钉钉机器人名称。
        :type ding_name: str
        :param offset: 分页列表的页数，默认值为0。取值范围大于等于0。
        :type offset: int
        :param limit: 分页返回结果，指定每页最大记录数。范围[1,100]，默认为10。  默认值：10
        :type limit: int
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._name = None
        self._remind_type = None
        self._ding_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if name is not None:
            self.name = name
        if remind_type is not None:
            self.remind_type = remind_type
        if ding_name is not None:
            self.ding_name = ding_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def workspace(self):
        r"""Gets the workspace of this ListFactoryAlarmRulesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListFactoryAlarmRulesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListFactoryAlarmRulesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListFactoryAlarmRulesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListFactoryAlarmRulesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListFactoryAlarmRulesRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListFactoryAlarmRulesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListFactoryAlarmRulesRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def name(self):
        r"""Gets the name of this ListFactoryAlarmRulesRequest.

        作业/规则名称。

        :return: The name of this ListFactoryAlarmRulesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFactoryAlarmRulesRequest.

        作业/规则名称。

        :param name: The name of this ListFactoryAlarmRulesRequest.
        :type name: str
        """
        self._name = name

    @property
    def remind_type(self):
        r"""Gets the remind_type of this ListFactoryAlarmRulesRequest.

        通知类型：  - 0：运行成功。 - 1：运行异常/失败。 - 3：未完成。 - 4：资源繁忙。 - 5：基线任务异常。 - 6：基线预警。 - 7：基线破线。 - 8：基线加剧。 - 9：保障作业预警时间未完成。 - 10：保障作业承诺时间未完成。 - 11：保障作业失败。 - 12：周期未完成。 - 13：运行取消。 - 14：失败作业重跑成功。 - 15：作业改动。 默认查询所有状态。

        :return: The remind_type of this ListFactoryAlarmRulesRequest.
        :rtype: int
        """
        return self._remind_type

    @remind_type.setter
    def remind_type(self, remind_type):
        r"""Sets the remind_type of this ListFactoryAlarmRulesRequest.

        通知类型：  - 0：运行成功。 - 1：运行异常/失败。 - 3：未完成。 - 4：资源繁忙。 - 5：基线任务异常。 - 6：基线预警。 - 7：基线破线。 - 8：基线加剧。 - 9：保障作业预警时间未完成。 - 10：保障作业承诺时间未完成。 - 11：保障作业失败。 - 12：周期未完成。 - 13：运行取消。 - 14：失败作业重跑成功。 - 15：作业改动。 默认查询所有状态。

        :param remind_type: The remind_type of this ListFactoryAlarmRulesRequest.
        :type remind_type: int
        """
        self._remind_type = remind_type

    @property
    def ding_name(self):
        r"""Gets the ding_name of this ListFactoryAlarmRulesRequest.

        钉钉机器人名称。

        :return: The ding_name of this ListFactoryAlarmRulesRequest.
        :rtype: str
        """
        return self._ding_name

    @ding_name.setter
    def ding_name(self, ding_name):
        r"""Sets the ding_name of this ListFactoryAlarmRulesRequest.

        钉钉机器人名称。

        :param ding_name: The ding_name of this ListFactoryAlarmRulesRequest.
        :type ding_name: str
        """
        self._ding_name = ding_name

    @property
    def offset(self):
        r"""Gets the offset of this ListFactoryAlarmRulesRequest.

        分页列表的页数，默认值为0。取值范围大于等于0。

        :return: The offset of this ListFactoryAlarmRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFactoryAlarmRulesRequest.

        分页列表的页数，默认值为0。取值范围大于等于0。

        :param offset: The offset of this ListFactoryAlarmRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFactoryAlarmRulesRequest.

        分页返回结果，指定每页最大记录数。范围[1,100]，默认为10。  默认值：10

        :return: The limit of this ListFactoryAlarmRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFactoryAlarmRulesRequest.

        分页返回结果，指定每页最大记录数。范围[1,100]，默认为10。  默认值：10

        :param limit: The limit of this ListFactoryAlarmRulesRequest.
        :type limit: int
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
        if not isinstance(other, ListFactoryAlarmRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
