# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobScriptOrderInfoModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_uuid': 'str',
        'gmt_created': 'int',
        'gmt_finished': 'int',
        'execute_costs': 'int',
        'creator': 'str',
        'status': 'str',
        'properties': 'JobScriptOrderInfoProp'
    }

    attribute_map = {
        'execute_uuid': 'execute_uuid',
        'gmt_created': 'gmt_created',
        'gmt_finished': 'gmt_finished',
        'execute_costs': 'execute_costs',
        'creator': 'creator',
        'status': 'status',
        'properties': 'properties'
    }

    def __init__(self, execute_uuid=None, gmt_created=None, gmt_finished=None, execute_costs=None, creator=None, status=None, properties=None):
        r"""JobScriptOrderInfoModel

        The model defined in huaweicloud sdk

        :param execute_uuid: 执行uuid
        :type execute_uuid: str
        :param gmt_created: 执行创建时间
        :type gmt_created: int
        :param gmt_finished: 执行完成时间
        :type gmt_finished: int
        :param execute_costs: 执行耗时，单位：秒
        :type execute_costs: int
        :param creator: 创建人
        :type creator: str
        :param status: 执行状态
        :type status: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkcoc.v1.JobScriptOrderInfoProp`
        """
        
        

        self._execute_uuid = None
        self._gmt_created = None
        self._gmt_finished = None
        self._execute_costs = None
        self._creator = None
        self._status = None
        self._properties = None
        self.discriminator = None

        if execute_uuid is not None:
            self.execute_uuid = execute_uuid
        if gmt_created is not None:
            self.gmt_created = gmt_created
        if gmt_finished is not None:
            self.gmt_finished = gmt_finished
        if execute_costs is not None:
            self.execute_costs = execute_costs
        if creator is not None:
            self.creator = creator
        if status is not None:
            self.status = status
        if properties is not None:
            self.properties = properties

    @property
    def execute_uuid(self):
        r"""Gets the execute_uuid of this JobScriptOrderInfoModel.

        执行uuid

        :return: The execute_uuid of this JobScriptOrderInfoModel.
        :rtype: str
        """
        return self._execute_uuid

    @execute_uuid.setter
    def execute_uuid(self, execute_uuid):
        r"""Sets the execute_uuid of this JobScriptOrderInfoModel.

        执行uuid

        :param execute_uuid: The execute_uuid of this JobScriptOrderInfoModel.
        :type execute_uuid: str
        """
        self._execute_uuid = execute_uuid

    @property
    def gmt_created(self):
        r"""Gets the gmt_created of this JobScriptOrderInfoModel.

        执行创建时间

        :return: The gmt_created of this JobScriptOrderInfoModel.
        :rtype: int
        """
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, gmt_created):
        r"""Sets the gmt_created of this JobScriptOrderInfoModel.

        执行创建时间

        :param gmt_created: The gmt_created of this JobScriptOrderInfoModel.
        :type gmt_created: int
        """
        self._gmt_created = gmt_created

    @property
    def gmt_finished(self):
        r"""Gets the gmt_finished of this JobScriptOrderInfoModel.

        执行完成时间

        :return: The gmt_finished of this JobScriptOrderInfoModel.
        :rtype: int
        """
        return self._gmt_finished

    @gmt_finished.setter
    def gmt_finished(self, gmt_finished):
        r"""Sets the gmt_finished of this JobScriptOrderInfoModel.

        执行完成时间

        :param gmt_finished: The gmt_finished of this JobScriptOrderInfoModel.
        :type gmt_finished: int
        """
        self._gmt_finished = gmt_finished

    @property
    def execute_costs(self):
        r"""Gets the execute_costs of this JobScriptOrderInfoModel.

        执行耗时，单位：秒

        :return: The execute_costs of this JobScriptOrderInfoModel.
        :rtype: int
        """
        return self._execute_costs

    @execute_costs.setter
    def execute_costs(self, execute_costs):
        r"""Sets the execute_costs of this JobScriptOrderInfoModel.

        执行耗时，单位：秒

        :param execute_costs: The execute_costs of this JobScriptOrderInfoModel.
        :type execute_costs: int
        """
        self._execute_costs = execute_costs

    @property
    def creator(self):
        r"""Gets the creator of this JobScriptOrderInfoModel.

        创建人

        :return: The creator of this JobScriptOrderInfoModel.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this JobScriptOrderInfoModel.

        创建人

        :param creator: The creator of this JobScriptOrderInfoModel.
        :type creator: str
        """
        self._creator = creator

    @property
    def status(self):
        r"""Gets the status of this JobScriptOrderInfoModel.

        执行状态

        :return: The status of this JobScriptOrderInfoModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobScriptOrderInfoModel.

        执行状态

        :param status: The status of this JobScriptOrderInfoModel.
        :type status: str
        """
        self._status = status

    @property
    def properties(self):
        r"""Gets the properties of this JobScriptOrderInfoModel.

        :return: The properties of this JobScriptOrderInfoModel.
        :rtype: :class:`huaweicloudsdkcoc.v1.JobScriptOrderInfoProp`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this JobScriptOrderInfoModel.

        :param properties: The properties of this JobScriptOrderInfoModel.
        :type properties: :class:`huaweicloudsdkcoc.v1.JobScriptOrderInfoProp`
        """
        self._properties = properties

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
        if not isinstance(other, JobScriptOrderInfoModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
