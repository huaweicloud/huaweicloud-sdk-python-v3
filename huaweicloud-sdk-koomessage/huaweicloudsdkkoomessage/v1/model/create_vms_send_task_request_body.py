# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVmsSendTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'tpl_id': 'str',
        'expiration_time': 'int',
        'mobiles': 'list[str]',
        'dync_params': 'list[ContentParam]',
        'individual_params': 'list[IndividualParam]',
        'exdata': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'tpl_id': 'tpl_id',
        'expiration_time': 'expiration_time',
        'mobiles': 'mobiles',
        'dync_params': 'dync_params',
        'individual_params': 'individual_params',
        'exdata': 'exdata'
    }

    def __init__(self, task_name=None, tpl_id=None, expiration_time=None, mobiles=None, dync_params=None, individual_params=None, exdata=None):
        """CreateVmsSendTaskRequestBody

        The model defined in huaweicloud sdk

        :param task_name: 任务名称。
        :type task_name: str
        :param tpl_id: 智能信息基础版模板ID。
        :type tpl_id: str
        :param expiration_time: 失效时间（小时，范围是1~72小时）。
        :type expiration_time: int
        :param mobiles: 群发手机号码列表，最多支持5000个号码。  &gt; 长度指的是单个号码的长度。 &gt; mobiles和individual_params字段只能二选一。 
        :type mobiles: list[str]
        :param dync_params: 群发动态参数数组。 - 参数顺序按照模板创建时参数占位符的顺序传入，例如创建模板时设置动参有#p_1#、#p_2#、#p_3#，则传入的参数数组顺序第一个元素为#p_1#，第二个元素是#p_2#，第三个元素为#p_3#。 - mobiles不填时，此字段被忽略。 
        :type dync_params: list[:class:`huaweicloudsdkkoomessage.v1.ContentParam`]
        :param individual_params: 个性化手机号码及动态参数数组。  mobiles和individual_params字段只能二选一。 
        :type individual_params: list[:class:`huaweicloudsdkkoomessage.v1.IndividualParam`]
        :param exdata: 智能信息基础版扩展字段。
        :type exdata: str
        """
        
        

        self._task_name = None
        self._tpl_id = None
        self._expiration_time = None
        self._mobiles = None
        self._dync_params = None
        self._individual_params = None
        self._exdata = None
        self.discriminator = None

        self.task_name = task_name
        self.tpl_id = tpl_id
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if mobiles is not None:
            self.mobiles = mobiles
        if dync_params is not None:
            self.dync_params = dync_params
        if individual_params is not None:
            self.individual_params = individual_params
        if exdata is not None:
            self.exdata = exdata

    @property
    def task_name(self):
        """Gets the task_name of this CreateVmsSendTaskRequestBody.

        任务名称。

        :return: The task_name of this CreateVmsSendTaskRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CreateVmsSendTaskRequestBody.

        任务名称。

        :param task_name: The task_name of this CreateVmsSendTaskRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def tpl_id(self):
        """Gets the tpl_id of this CreateVmsSendTaskRequestBody.

        智能信息基础版模板ID。

        :return: The tpl_id of this CreateVmsSendTaskRequestBody.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this CreateVmsSendTaskRequestBody.

        智能信息基础版模板ID。

        :param tpl_id: The tpl_id of this CreateVmsSendTaskRequestBody.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def expiration_time(self):
        """Gets the expiration_time of this CreateVmsSendTaskRequestBody.

        失效时间（小时，范围是1~72小时）。

        :return: The expiration_time of this CreateVmsSendTaskRequestBody.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this CreateVmsSendTaskRequestBody.

        失效时间（小时，范围是1~72小时）。

        :param expiration_time: The expiration_time of this CreateVmsSendTaskRequestBody.
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

    @property
    def mobiles(self):
        """Gets the mobiles of this CreateVmsSendTaskRequestBody.

        群发手机号码列表，最多支持5000个号码。  > 长度指的是单个号码的长度。 > mobiles和individual_params字段只能二选一。 

        :return: The mobiles of this CreateVmsSendTaskRequestBody.
        :rtype: list[str]
        """
        return self._mobiles

    @mobiles.setter
    def mobiles(self, mobiles):
        """Sets the mobiles of this CreateVmsSendTaskRequestBody.

        群发手机号码列表，最多支持5000个号码。  > 长度指的是单个号码的长度。 > mobiles和individual_params字段只能二选一。 

        :param mobiles: The mobiles of this CreateVmsSendTaskRequestBody.
        :type mobiles: list[str]
        """
        self._mobiles = mobiles

    @property
    def dync_params(self):
        """Gets the dync_params of this CreateVmsSendTaskRequestBody.

        群发动态参数数组。 - 参数顺序按照模板创建时参数占位符的顺序传入，例如创建模板时设置动参有#p_1#、#p_2#、#p_3#，则传入的参数数组顺序第一个元素为#p_1#，第二个元素是#p_2#，第三个元素为#p_3#。 - mobiles不填时，此字段被忽略。 

        :return: The dync_params of this CreateVmsSendTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.ContentParam`]
        """
        return self._dync_params

    @dync_params.setter
    def dync_params(self, dync_params):
        """Sets the dync_params of this CreateVmsSendTaskRequestBody.

        群发动态参数数组。 - 参数顺序按照模板创建时参数占位符的顺序传入，例如创建模板时设置动参有#p_1#、#p_2#、#p_3#，则传入的参数数组顺序第一个元素为#p_1#，第二个元素是#p_2#，第三个元素为#p_3#。 - mobiles不填时，此字段被忽略。 

        :param dync_params: The dync_params of this CreateVmsSendTaskRequestBody.
        :type dync_params: list[:class:`huaweicloudsdkkoomessage.v1.ContentParam`]
        """
        self._dync_params = dync_params

    @property
    def individual_params(self):
        """Gets the individual_params of this CreateVmsSendTaskRequestBody.

        个性化手机号码及动态参数数组。  mobiles和individual_params字段只能二选一。 

        :return: The individual_params of this CreateVmsSendTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.IndividualParam`]
        """
        return self._individual_params

    @individual_params.setter
    def individual_params(self, individual_params):
        """Sets the individual_params of this CreateVmsSendTaskRequestBody.

        个性化手机号码及动态参数数组。  mobiles和individual_params字段只能二选一。 

        :param individual_params: The individual_params of this CreateVmsSendTaskRequestBody.
        :type individual_params: list[:class:`huaweicloudsdkkoomessage.v1.IndividualParam`]
        """
        self._individual_params = individual_params

    @property
    def exdata(self):
        """Gets the exdata of this CreateVmsSendTaskRequestBody.

        智能信息基础版扩展字段。

        :return: The exdata of this CreateVmsSendTaskRequestBody.
        :rtype: str
        """
        return self._exdata

    @exdata.setter
    def exdata(self, exdata):
        """Sets the exdata of this CreateVmsSendTaskRequestBody.

        智能信息基础版扩展字段。

        :param exdata: The exdata of this CreateVmsSendTaskRequestBody.
        :type exdata: str
        """
        self._exdata = exdata

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
        if not isinstance(other, CreateVmsSendTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
