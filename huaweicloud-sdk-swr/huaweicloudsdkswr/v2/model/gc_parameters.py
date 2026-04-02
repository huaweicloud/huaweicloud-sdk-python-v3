# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GcParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_untagged': 'bool',
        'workers': 'int',
        'dry_run': 'bool'
    }

    attribute_map = {
        'delete_untagged': 'delete_untagged',
        'workers': 'workers',
        'dry_run': 'dry_run'
    }

    def __init__(self, delete_untagged=None, workers=None, dry_run=None):
        r"""GcParameters

        The model defined in huaweicloud sdk

        :param delete_untagged: 是否删除无tag的制品；默认为false，不删除无tag的制品。
        :type delete_untagged: bool
        :param workers: 并行执行制品清理任务的工作者数量，最小值为1，最大值为5。
        :type workers: int
        :param dry_run: 是否模拟执行任务；默认值为false，非模拟运行。
        :type dry_run: bool
        """
        
        

        self._delete_untagged = None
        self._workers = None
        self._dry_run = None
        self.discriminator = None

        if delete_untagged is not None:
            self.delete_untagged = delete_untagged
        self.workers = workers
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def delete_untagged(self):
        r"""Gets the delete_untagged of this GcParameters.

        是否删除无tag的制品；默认为false，不删除无tag的制品。

        :return: The delete_untagged of this GcParameters.
        :rtype: bool
        """
        return self._delete_untagged

    @delete_untagged.setter
    def delete_untagged(self, delete_untagged):
        r"""Sets the delete_untagged of this GcParameters.

        是否删除无tag的制品；默认为false，不删除无tag的制品。

        :param delete_untagged: The delete_untagged of this GcParameters.
        :type delete_untagged: bool
        """
        self._delete_untagged = delete_untagged

    @property
    def workers(self):
        r"""Gets the workers of this GcParameters.

        并行执行制品清理任务的工作者数量，最小值为1，最大值为5。

        :return: The workers of this GcParameters.
        :rtype: int
        """
        return self._workers

    @workers.setter
    def workers(self, workers):
        r"""Sets the workers of this GcParameters.

        并行执行制品清理任务的工作者数量，最小值为1，最大值为5。

        :param workers: The workers of this GcParameters.
        :type workers: int
        """
        self._workers = workers

    @property
    def dry_run(self):
        r"""Gets the dry_run of this GcParameters.

        是否模拟执行任务；默认值为false，非模拟运行。

        :return: The dry_run of this GcParameters.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this GcParameters.

        是否模拟执行任务；默认值为false，非模拟运行。

        :param dry_run: The dry_run of this GcParameters.
        :type dry_run: bool
        """
        self._dry_run = dry_run

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
        if not isinstance(other, GcParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
