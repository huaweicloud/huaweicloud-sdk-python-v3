# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisSummaryItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'progress': 'int',
        'status': 'str',
        'normal_item_num': 'int',
        'abnormal_item_num': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'progress': 'progress',
        'status': 'status',
        'normal_item_num': 'normal_item_num',
        'abnormal_item_num': 'abnormal_item_num'
    }

    def __init__(self, instance_id=None, instance_name=None, progress=None, status=None, normal_item_num=None, abnormal_item_num=None):
        r"""DiagnosisSummaryItem

        The model defined in huaweicloud sdk

        :param instance_id: 被诊断实例的ID
        :type instance_id: str
        :param instance_name: 被诊断实例的名称
        :type instance_name: str
        :param progress: 被诊断实例的诊断进度
        :type progress: int
        :param status: 诊断任务状态，waiting,executing,failed,finish,cancel
        :type status: str
        :param normal_item_num: 实例的正常诊断项数量
        :type normal_item_num: int
        :param abnormal_item_num: 实例的异常诊断项数量
        :type abnormal_item_num: int
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._progress = None
        self._status = None
        self._normal_item_num = None
        self._abnormal_item_num = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status
        if normal_item_num is not None:
            self.normal_item_num = normal_item_num
        if abnormal_item_num is not None:
            self.abnormal_item_num = abnormal_item_num

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DiagnosisSummaryItem.

        被诊断实例的ID

        :return: The instance_id of this DiagnosisSummaryItem.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DiagnosisSummaryItem.

        被诊断实例的ID

        :param instance_id: The instance_id of this DiagnosisSummaryItem.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DiagnosisSummaryItem.

        被诊断实例的名称

        :return: The instance_name of this DiagnosisSummaryItem.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DiagnosisSummaryItem.

        被诊断实例的名称

        :param instance_name: The instance_name of this DiagnosisSummaryItem.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def progress(self):
        r"""Gets the progress of this DiagnosisSummaryItem.

        被诊断实例的诊断进度

        :return: The progress of this DiagnosisSummaryItem.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this DiagnosisSummaryItem.

        被诊断实例的诊断进度

        :param progress: The progress of this DiagnosisSummaryItem.
        :type progress: int
        """
        self._progress = progress

    @property
    def status(self):
        r"""Gets the status of this DiagnosisSummaryItem.

        诊断任务状态，waiting,executing,failed,finish,cancel

        :return: The status of this DiagnosisSummaryItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DiagnosisSummaryItem.

        诊断任务状态，waiting,executing,failed,finish,cancel

        :param status: The status of this DiagnosisSummaryItem.
        :type status: str
        """
        self._status = status

    @property
    def normal_item_num(self):
        r"""Gets the normal_item_num of this DiagnosisSummaryItem.

        实例的正常诊断项数量

        :return: The normal_item_num of this DiagnosisSummaryItem.
        :rtype: int
        """
        return self._normal_item_num

    @normal_item_num.setter
    def normal_item_num(self, normal_item_num):
        r"""Sets the normal_item_num of this DiagnosisSummaryItem.

        实例的正常诊断项数量

        :param normal_item_num: The normal_item_num of this DiagnosisSummaryItem.
        :type normal_item_num: int
        """
        self._normal_item_num = normal_item_num

    @property
    def abnormal_item_num(self):
        r"""Gets the abnormal_item_num of this DiagnosisSummaryItem.

        实例的异常诊断项数量

        :return: The abnormal_item_num of this DiagnosisSummaryItem.
        :rtype: int
        """
        return self._abnormal_item_num

    @abnormal_item_num.setter
    def abnormal_item_num(self, abnormal_item_num):
        r"""Sets the abnormal_item_num of this DiagnosisSummaryItem.

        实例的异常诊断项数量

        :param abnormal_item_num: The abnormal_item_num of this DiagnosisSummaryItem.
        :type abnormal_item_num: int
        """
        self._abnormal_item_num = abnormal_item_num

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
        if not isinstance(other, DiagnosisSummaryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
