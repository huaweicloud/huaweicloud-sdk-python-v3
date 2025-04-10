# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordJobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deploy_type': 'str',
        'source_url': 'str',
        'first_batch_weight': 'int',
        'first_batch_replica': 'int',
        'replica': 'int',
        'remaining_batch': 'int'
    }

    attribute_map = {
        'deploy_type': 'deploy_type',
        'source_url': 'source_url',
        'first_batch_weight': 'first_batch_weight',
        'first_batch_replica': 'first_batch_replica',
        'replica': 'replica',
        'remaining_batch': 'remaining_batch'
    }

    def __init__(self, deploy_type=None, source_url=None, first_batch_weight=None, first_batch_replica=None, replica=None, remaining_batch=None):
        r"""RecordJobInfo

        The model defined in huaweicloud sdk

        :param deploy_type: 
        :type deploy_type: str
        :param source_url: 组件来源的url
        :type source_url: str
        :param first_batch_weight: 
        :type first_batch_weight: int
        :param first_batch_replica: 
        :type first_batch_replica: int
        :param replica: 
        :type replica: int
        :param remaining_batch: 
        :type remaining_batch: int
        """
        
        

        self._deploy_type = None
        self._source_url = None
        self._first_batch_weight = None
        self._first_batch_replica = None
        self._replica = None
        self._remaining_batch = None
        self.discriminator = None

        if deploy_type is not None:
            self.deploy_type = deploy_type
        if source_url is not None:
            self.source_url = source_url
        if first_batch_weight is not None:
            self.first_batch_weight = first_batch_weight
        if first_batch_replica is not None:
            self.first_batch_replica = first_batch_replica
        if replica is not None:
            self.replica = replica
        if remaining_batch is not None:
            self.remaining_batch = remaining_batch

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this RecordJobInfo.

        :return: The deploy_type of this RecordJobInfo.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this RecordJobInfo.

        :param deploy_type: The deploy_type of this RecordJobInfo.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def source_url(self):
        r"""Gets the source_url of this RecordJobInfo.

        组件来源的url

        :return: The source_url of this RecordJobInfo.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        r"""Sets the source_url of this RecordJobInfo.

        组件来源的url

        :param source_url: The source_url of this RecordJobInfo.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def first_batch_weight(self):
        r"""Gets the first_batch_weight of this RecordJobInfo.

        :return: The first_batch_weight of this RecordJobInfo.
        :rtype: int
        """
        return self._first_batch_weight

    @first_batch_weight.setter
    def first_batch_weight(self, first_batch_weight):
        r"""Sets the first_batch_weight of this RecordJobInfo.

        :param first_batch_weight: The first_batch_weight of this RecordJobInfo.
        :type first_batch_weight: int
        """
        self._first_batch_weight = first_batch_weight

    @property
    def first_batch_replica(self):
        r"""Gets the first_batch_replica of this RecordJobInfo.

        :return: The first_batch_replica of this RecordJobInfo.
        :rtype: int
        """
        return self._first_batch_replica

    @first_batch_replica.setter
    def first_batch_replica(self, first_batch_replica):
        r"""Sets the first_batch_replica of this RecordJobInfo.

        :param first_batch_replica: The first_batch_replica of this RecordJobInfo.
        :type first_batch_replica: int
        """
        self._first_batch_replica = first_batch_replica

    @property
    def replica(self):
        r"""Gets the replica of this RecordJobInfo.

        :return: The replica of this RecordJobInfo.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        r"""Sets the replica of this RecordJobInfo.

        :param replica: The replica of this RecordJobInfo.
        :type replica: int
        """
        self._replica = replica

    @property
    def remaining_batch(self):
        r"""Gets the remaining_batch of this RecordJobInfo.

        :return: The remaining_batch of this RecordJobInfo.
        :rtype: int
        """
        return self._remaining_batch

    @remaining_batch.setter
    def remaining_batch(self, remaining_batch):
        r"""Sets the remaining_batch of this RecordJobInfo.

        :param remaining_batch: The remaining_batch of this RecordJobInfo.
        :type remaining_batch: int
        """
        self._remaining_batch = remaining_batch

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
        if not isinstance(other, RecordJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
