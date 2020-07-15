# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListNumberOfInstancesInDifferentStatusResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'redis': 'StatusStatistic',
        'memcached': 'StatusStatistic',
        'paying_count': 'int',
        'freezing_count': 'int',
        'migrating_count': 'int',
        'flushing_count': 'int',
        'upgrading_count': 'int',
        'restoring_count': 'int',
        'extending_count': 'int',
        'creating_count': 'int',
        'running_count': 'int',
        'error_count': 'int',
        'frozen_count': 'int',
        'createfailed_count': 'int',
        'restarting_count': 'int'
    }

    attribute_map = {
        'redis': 'redis',
        'memcached': 'memcached',
        'paying_count': 'paying_count',
        'freezing_count': 'freezing_count',
        'migrating_count': 'migrating_count',
        'flushing_count': 'flushing_count',
        'upgrading_count': 'upgrading_count',
        'restoring_count': 'restoring_count',
        'extending_count': 'extending_count',
        'creating_count': 'creating_count',
        'running_count': 'running_count',
        'error_count': 'error_count',
        'frozen_count': 'frozen_count',
        'createfailed_count': 'createfailed_count',
        'restarting_count': 'restarting_count'
    }

    def __init__(self, redis=None, memcached=None, paying_count=None, freezing_count=None, migrating_count=None, flushing_count=None, upgrading_count=None, restoring_count=None, extending_count=None, creating_count=None, running_count=None, error_count=None, frozen_count=None, createfailed_count=None, restarting_count=None):
        """ListNumberOfInstancesInDifferentStatusResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._redis = None
        self._memcached = None
        self._paying_count = None
        self._freezing_count = None
        self._migrating_count = None
        self._flushing_count = None
        self._upgrading_count = None
        self._restoring_count = None
        self._extending_count = None
        self._creating_count = None
        self._running_count = None
        self._error_count = None
        self._frozen_count = None
        self._createfailed_count = None
        self._restarting_count = None
        self.discriminator = None

        if redis is not None:
            self.redis = redis
        if memcached is not None:
            self.memcached = memcached
        if paying_count is not None:
            self.paying_count = paying_count
        if freezing_count is not None:
            self.freezing_count = freezing_count
        if migrating_count is not None:
            self.migrating_count = migrating_count
        if flushing_count is not None:
            self.flushing_count = flushing_count
        if upgrading_count is not None:
            self.upgrading_count = upgrading_count
        if restoring_count is not None:
            self.restoring_count = restoring_count
        if extending_count is not None:
            self.extending_count = extending_count
        if creating_count is not None:
            self.creating_count = creating_count
        if running_count is not None:
            self.running_count = running_count
        if error_count is not None:
            self.error_count = error_count
        if frozen_count is not None:
            self.frozen_count = frozen_count
        if createfailed_count is not None:
            self.createfailed_count = createfailed_count
        if restarting_count is not None:
            self.restarting_count = restarting_count

    @property
    def redis(self):
        """Gets the redis of this ListNumberOfInstancesInDifferentStatusResponse.


        :return: The redis of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: StatusStatistic
        """
        return self._redis

    @redis.setter
    def redis(self, redis):
        """Sets the redis of this ListNumberOfInstancesInDifferentStatusResponse.


        :param redis: The redis of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: StatusStatistic
        """
        self._redis = redis

    @property
    def memcached(self):
        """Gets the memcached of this ListNumberOfInstancesInDifferentStatusResponse.


        :return: The memcached of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: StatusStatistic
        """
        return self._memcached

    @memcached.setter
    def memcached(self, memcached):
        """Sets the memcached of this ListNumberOfInstancesInDifferentStatusResponse.


        :param memcached: The memcached of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: StatusStatistic
        """
        self._memcached = memcached

    @property
    def paying_count(self):
        """Gets the paying_count of this ListNumberOfInstancesInDifferentStatusResponse.

        支付中的实例数。

        :return: The paying_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._paying_count

    @paying_count.setter
    def paying_count(self, paying_count):
        """Sets the paying_count of this ListNumberOfInstancesInDifferentStatusResponse.

        支付中的实例数。

        :param paying_count: The paying_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._paying_count = paying_count

    @property
    def freezing_count(self):
        """Gets the freezing_count of this ListNumberOfInstancesInDifferentStatusResponse.

        冻结中的实例数。

        :return: The freezing_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._freezing_count

    @freezing_count.setter
    def freezing_count(self, freezing_count):
        """Sets the freezing_count of this ListNumberOfInstancesInDifferentStatusResponse.

        冻结中的实例数。

        :param freezing_count: The freezing_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._freezing_count = freezing_count

    @property
    def migrating_count(self):
        """Gets the migrating_count of this ListNumberOfInstancesInDifferentStatusResponse.

        迁移中的实例数。

        :return: The migrating_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._migrating_count

    @migrating_count.setter
    def migrating_count(self, migrating_count):
        """Sets the migrating_count of this ListNumberOfInstancesInDifferentStatusResponse.

        迁移中的实例数。

        :param migrating_count: The migrating_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._migrating_count = migrating_count

    @property
    def flushing_count(self):
        """Gets the flushing_count of this ListNumberOfInstancesInDifferentStatusResponse.

        清空中的实例数。

        :return: The flushing_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._flushing_count

    @flushing_count.setter
    def flushing_count(self, flushing_count):
        """Sets the flushing_count of this ListNumberOfInstancesInDifferentStatusResponse.

        清空中的实例数。

        :param flushing_count: The flushing_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._flushing_count = flushing_count

    @property
    def upgrading_count(self):
        """Gets the upgrading_count of this ListNumberOfInstancesInDifferentStatusResponse.

        升级中的实例数。

        :return: The upgrading_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._upgrading_count

    @upgrading_count.setter
    def upgrading_count(self, upgrading_count):
        """Sets the upgrading_count of this ListNumberOfInstancesInDifferentStatusResponse.

        升级中的实例数。

        :param upgrading_count: The upgrading_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._upgrading_count = upgrading_count

    @property
    def restoring_count(self):
        """Gets the restoring_count of this ListNumberOfInstancesInDifferentStatusResponse.

        恢复中的实例数。

        :return: The restoring_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._restoring_count

    @restoring_count.setter
    def restoring_count(self, restoring_count):
        """Sets the restoring_count of this ListNumberOfInstancesInDifferentStatusResponse.

        恢复中的实例数。

        :param restoring_count: The restoring_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._restoring_count = restoring_count

    @property
    def extending_count(self):
        """Gets the extending_count of this ListNumberOfInstancesInDifferentStatusResponse.

        扩容中的实例数。

        :return: The extending_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._extending_count

    @extending_count.setter
    def extending_count(self, extending_count):
        """Sets the extending_count of this ListNumberOfInstancesInDifferentStatusResponse.

        扩容中的实例数。

        :param extending_count: The extending_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._extending_count = extending_count

    @property
    def creating_count(self):
        """Gets the creating_count of this ListNumberOfInstancesInDifferentStatusResponse.

        正在创建的实例数。

        :return: The creating_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._creating_count

    @creating_count.setter
    def creating_count(self, creating_count):
        """Sets the creating_count of this ListNumberOfInstancesInDifferentStatusResponse.

        正在创建的实例数。

        :param creating_count: The creating_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._creating_count = creating_count

    @property
    def running_count(self):
        """Gets the running_count of this ListNumberOfInstancesInDifferentStatusResponse.

        正在运行的实例数。

        :return: The running_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        """Sets the running_count of this ListNumberOfInstancesInDifferentStatusResponse.

        正在运行的实例数。

        :param running_count: The running_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._running_count = running_count

    @property
    def error_count(self):
        """Gets the error_count of this ListNumberOfInstancesInDifferentStatusResponse.

        异常的实例数。

        :return: The error_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this ListNumberOfInstancesInDifferentStatusResponse.

        异常的实例数。

        :param error_count: The error_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._error_count = error_count

    @property
    def frozen_count(self):
        """Gets the frozen_count of this ListNumberOfInstancesInDifferentStatusResponse.

        已冻结的实例数。

        :return: The frozen_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._frozen_count

    @frozen_count.setter
    def frozen_count(self, frozen_count):
        """Sets the frozen_count of this ListNumberOfInstancesInDifferentStatusResponse.

        已冻结的实例数。

        :param frozen_count: The frozen_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._frozen_count = frozen_count

    @property
    def createfailed_count(self):
        """Gets the createfailed_count of this ListNumberOfInstancesInDifferentStatusResponse.

        创建失败的实例数。

        :return: The createfailed_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._createfailed_count

    @createfailed_count.setter
    def createfailed_count(self, createfailed_count):
        """Sets the createfailed_count of this ListNumberOfInstancesInDifferentStatusResponse.

        创建失败的实例数。

        :param createfailed_count: The createfailed_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._createfailed_count = createfailed_count

    @property
    def restarting_count(self):
        """Gets the restarting_count of this ListNumberOfInstancesInDifferentStatusResponse.

        正在重启的实例数。

        :return: The restarting_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :rtype: int
        """
        return self._restarting_count

    @restarting_count.setter
    def restarting_count(self, restarting_count):
        """Sets the restarting_count of this ListNumberOfInstancesInDifferentStatusResponse.

        正在重启的实例数。

        :param restarting_count: The restarting_count of this ListNumberOfInstancesInDifferentStatusResponse.
        :type: int
        """
        self._restarting_count = restarting_count

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListNumberOfInstancesInDifferentStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
