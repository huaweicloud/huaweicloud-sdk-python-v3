# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetBackupPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'succeeded_num': 'int',
        'failed_num': 'int',
        'failed_instances': 'list[BatchSetBackupPolicyFailedRecordResult]'
    }

    attribute_map = {
        'succeeded_num': 'succeeded_num',
        'failed_num': 'failed_num',
        'failed_instances': 'failed_instances'
    }

    def __init__(self, succeeded_num=None, failed_num=None, failed_instances=None):
        r"""BatchSetBackupPolicyResponse

        The model defined in huaweicloud sdk

        :param succeeded_num: **参数解释**: 设置成功的实例数量。 **取值范围**: 不涉及。
        :type succeeded_num: int
        :param failed_num: **参数解释**: 设置失败的实例数量。 **取值范围**: 不涉及。
        :type failed_num: int
        :param failed_instances: **参数解释**: 设置失败的实例记录。
        :type failed_instances: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.BatchSetBackupPolicyFailedRecordResult`]
        """
        
        super(BatchSetBackupPolicyResponse, self).__init__()

        self._succeeded_num = None
        self._failed_num = None
        self._failed_instances = None
        self.discriminator = None

        if succeeded_num is not None:
            self.succeeded_num = succeeded_num
        if failed_num is not None:
            self.failed_num = failed_num
        if failed_instances is not None:
            self.failed_instances = failed_instances

    @property
    def succeeded_num(self):
        r"""Gets the succeeded_num of this BatchSetBackupPolicyResponse.

        **参数解释**: 设置成功的实例数量。 **取值范围**: 不涉及。

        :return: The succeeded_num of this BatchSetBackupPolicyResponse.
        :rtype: int
        """
        return self._succeeded_num

    @succeeded_num.setter
    def succeeded_num(self, succeeded_num):
        r"""Sets the succeeded_num of this BatchSetBackupPolicyResponse.

        **参数解释**: 设置成功的实例数量。 **取值范围**: 不涉及。

        :param succeeded_num: The succeeded_num of this BatchSetBackupPolicyResponse.
        :type succeeded_num: int
        """
        self._succeeded_num = succeeded_num

    @property
    def failed_num(self):
        r"""Gets the failed_num of this BatchSetBackupPolicyResponse.

        **参数解释**: 设置失败的实例数量。 **取值范围**: 不涉及。

        :return: The failed_num of this BatchSetBackupPolicyResponse.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this BatchSetBackupPolicyResponse.

        **参数解释**: 设置失败的实例数量。 **取值范围**: 不涉及。

        :param failed_num: The failed_num of this BatchSetBackupPolicyResponse.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def failed_instances(self):
        r"""Gets the failed_instances of this BatchSetBackupPolicyResponse.

        **参数解释**: 设置失败的实例记录。

        :return: The failed_instances of this BatchSetBackupPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.BatchSetBackupPolicyFailedRecordResult`]
        """
        return self._failed_instances

    @failed_instances.setter
    def failed_instances(self, failed_instances):
        r"""Sets the failed_instances of this BatchSetBackupPolicyResponse.

        **参数解释**: 设置失败的实例记录。

        :param failed_instances: The failed_instances of this BatchSetBackupPolicyResponse.
        :type failed_instances: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.BatchSetBackupPolicyFailedRecordResult`]
        """
        self._failed_instances = failed_instances

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
        if not isinstance(other, BatchSetBackupPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
