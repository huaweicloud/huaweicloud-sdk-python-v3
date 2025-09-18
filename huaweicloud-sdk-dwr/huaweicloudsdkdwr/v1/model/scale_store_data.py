# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleStoreData:

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
        'job_id': 'str',
        'store_name': 'str',
        'status': 'str',
        'cu_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'job_id': 'job_id',
        'store_name': 'store_name',
        'status': 'status',
        'cu_num': 'cu_num'
    }

    def __init__(self, id=None, job_id=None, store_name=None, status=None, cu_num=None):
        r"""ScaleStoreData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 知识仓实例id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type id: str
        :param job_id: **参数解释：** 创建知识仓实例的任务id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type job_id: str
        :param store_name: **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type store_name: str
        :param status: **参数解释：** 知识仓实例状态。 **约束限制：** 不涉及。 **取值范围：** CREATING：创建中 NORMAL：正常 CREATED_FAILED：创建失败 ABNORMAL：异常 FROZEN：冻结 DISK_FULL：存储空间已满 DELETING：删除中 DELETE_FAILED：删除失败 SCALING：扩容中 **默认取值:** 不涉及。
        :type status: str
        :param cu_num: **参数解释：** 扩容后cu规格的数量 **约束限制：** cu_num值要大于当前已有cu规格的数量 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cu_num: int
        """
        
        

        self._id = None
        self._job_id = None
        self._store_name = None
        self._status = None
        self._cu_num = None
        self.discriminator = None

        self.id = id
        self.job_id = job_id
        self.store_name = store_name
        self.status = status
        if cu_num is not None:
            self.cu_num = cu_num

    @property
    def id(self):
        r"""Gets the id of this ScaleStoreData.

        **参数解释：** 知识仓实例id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The id of this ScaleStoreData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScaleStoreData.

        **参数解释：** 知识仓实例id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param id: The id of this ScaleStoreData.
        :type id: str
        """
        self._id = id

    @property
    def job_id(self):
        r"""Gets the job_id of this ScaleStoreData.

        **参数解释：** 创建知识仓实例的任务id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The job_id of this ScaleStoreData.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ScaleStoreData.

        **参数解释：** 创建知识仓实例的任务id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param job_id: The job_id of this ScaleStoreData.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def store_name(self):
        r"""Gets the store_name of this ScaleStoreData.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The store_name of this ScaleStoreData.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this ScaleStoreData.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param store_name: The store_name of this ScaleStoreData.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def status(self):
        r"""Gets the status of this ScaleStoreData.

        **参数解释：** 知识仓实例状态。 **约束限制：** 不涉及。 **取值范围：** CREATING：创建中 NORMAL：正常 CREATED_FAILED：创建失败 ABNORMAL：异常 FROZEN：冻结 DISK_FULL：存储空间已满 DELETING：删除中 DELETE_FAILED：删除失败 SCALING：扩容中 **默认取值:** 不涉及。

        :return: The status of this ScaleStoreData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScaleStoreData.

        **参数解释：** 知识仓实例状态。 **约束限制：** 不涉及。 **取值范围：** CREATING：创建中 NORMAL：正常 CREATED_FAILED：创建失败 ABNORMAL：异常 FROZEN：冻结 DISK_FULL：存储空间已满 DELETING：删除中 DELETE_FAILED：删除失败 SCALING：扩容中 **默认取值:** 不涉及。

        :param status: The status of this ScaleStoreData.
        :type status: str
        """
        self._status = status

    @property
    def cu_num(self):
        r"""Gets the cu_num of this ScaleStoreData.

        **参数解释：** 扩容后cu规格的数量 **约束限制：** cu_num值要大于当前已有cu规格的数量 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cu_num of this ScaleStoreData.
        :rtype: int
        """
        return self._cu_num

    @cu_num.setter
    def cu_num(self, cu_num):
        r"""Sets the cu_num of this ScaleStoreData.

        **参数解释：** 扩容后cu规格的数量 **约束限制：** cu_num值要大于当前已有cu规格的数量 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cu_num: The cu_num of this ScaleStoreData.
        :type cu_num: int
        """
        self._cu_num = cu_num

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
        if not isinstance(other, ScaleStoreData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
