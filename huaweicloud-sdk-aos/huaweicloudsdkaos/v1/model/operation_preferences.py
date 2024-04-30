# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationPreferences:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_concurrency_type': 'str',
        'region_order': 'list[str]',
        'failure_tolerance_count': 'int',
        'failure_tolerance_percentage': 'int',
        'max_concurrent_count': 'int',
        'max_concurrent_percentage': 'int',
        'failure_tolerance_mode': 'str'
    }

    attribute_map = {
        'region_concurrency_type': 'region_concurrency_type',
        'region_order': 'region_order',
        'failure_tolerance_count': 'failure_tolerance_count',
        'failure_tolerance_percentage': 'failure_tolerance_percentage',
        'max_concurrent_count': 'max_concurrent_count',
        'max_concurrent_percentage': 'max_concurrent_percentage',
        'failure_tolerance_mode': 'failure_tolerance_mode'
    }

    def __init__(self, region_concurrency_type=None, region_order=None, failure_tolerance_count=None, failure_tolerance_percentage=None, max_concurrent_count=None, max_concurrent_percentage=None, failure_tolerance_mode=None):
        """OperationPreferences

        The model defined in huaweicloud sdk

        :param region_concurrency_type: 部署资源栈实例时区域（region）的执行策略，分为两种，SEQUENTIAL和PARALLEL，区分大小写，默认值为SEQUENTIAL  详细介绍：  * &#x60;SEQUENTIAL&#x60;：顺序执行，执行完一个region下的全部资源栈实例后再去执行另一个region。默认顺序执行。  * &#x60;PARALLEL&#x60;：并发执行，并发部署所有指定区域的资源栈实例。
        :type region_concurrency_type: str
        :param region_order: 区域（region）部署顺序。只有当用户指定region_concurrency_type为SEQUENTIAL时才会允许指定该参数。用户指定部署region的顺序，不允许出现资源栈集管理之外的region。  如果不指定，实际部署region顺序随机。部署顺序仅在当次部署时生效，应该包含且仅包含本次部署的所有region。
        :type region_order: list[str]
        :param failure_tolerance_count: 容错次数。用户定义在每个区域（region）下，允许部署失败的资源栈实例数量。该参数取值默认为0，限定0和正整数。  如果定义region顺序执行（region_concurrency_type值为SEQUENTIAL），在某个region超过容错次数时，资源栈集会取消所有状态仍处于WAIT_IN_PROGRESS状态的实例。被取消的实例状态最终变为CANCEL_COMPLETE；  如果是region并行执行（region_concurrency_type值为PARALLEL），在某个region超过容错次数时，资源栈集只会取消该region下所有处于WAIT_IN_PROGRESS状态的实例。被取消的实例状态最终变为CANCEL_COMPLETE。  对处于OPERATION_IN_PROGRESS，或已经部署完成，即处于OPERATION_COMPLETE或者OPERATION_FAILED状态的资源栈实例，不受影响，状态不变。  failure_tolerance_count  和 failure_tolerance_percentage 仅能有一个存在。
        :type failure_tolerance_count: int
        :param failure_tolerance_percentage: 容错百分比。定义每个区域（region）下，允许部署失败的资源栈实例数占该region下所有资源栈实例数的百分比。该参数取值默认为0，限定0和正整数。  通过容错百分比*资源栈实例数，并向下取整，得到实际容错次数。  failure_tolerance_count  和 failure_tolerance_percentage 仅能有一个存在。
        :type failure_tolerance_percentage: int
        :param max_concurrent_count: 每个区域（region）下可同时部署资源栈实例的最大账户数。该参数取值默认为1，限定为正整数。  最大并发账户数最多比容错次数多1。如果用户指定failure_tolerance_percentage，最大并发账户数最多比 failure_tolerance_percentage * 资源栈实例数多1。保证部署在所需的容错级别停止。  max_concurrent_count 和 max_concurrent_percentage 仅能有一个存在。
        :type max_concurrent_count: int
        :param max_concurrent_percentage: 最大并发账户百分比，每个区域（region）中可同时部署的资源栈实例的最大账户百分比。该参数取值默认为1，限定正整数。  RFS根据百分比 *（每个region下资源栈实例数）得到的值，再向下取整，得到实际最大并发账户数。如果实际最大并发账户数向下取整值为0时，则默认选择最大并发账户数为1。  通过百分比计算得到的实际最大并发账户数最多比容错次数多1。如果用户指定failure_tolerance_percentage，实际最大并发账户数最多比 failure_tolerance_percentage * 资源栈实例数多1。保证部署在所需的容错级别停止。  max_concurrent_count 和 max_concurrent_percentage 仅能有一个存在。
        :type max_concurrent_percentage: int
        :param failure_tolerance_mode: 资源栈集操作部署的失败容忍模式，分为两种，STRICT_FAILURE_TOLERANCE和SOFT_FAILURE_TOLERANCE，区分大小写，默认值为STRICT_FAILURE_TOLERANCE。  详细介绍：  * &#x60;STRICT_FAILURE_TOLERANCE&#x60;：此选项会动态降低并发级别，以确保同region下部署失败的账户数量永远不超过 failure_tolerance_count + 1。当用户指定failure_tolerance_percentage时，确保同region下部署失败的账户数量不超过 failure_tolerance_percentage * 资源栈实例数 + 1。  * 初始实际最大并发数为max_concurrent_count，如果用户指定的是max_concurrent_percentage，则初始实际最大并发数为 max_concurrent_percentage * 资源栈实例数，随后，实际最大并发数会根据失败次数增加而减少。  * &#x60;SOFT_FAILURE_TOLERANCE&#x60;：此选项将failure_tolerance_count (failure_tolerance_percentage) 与实际并发数分离开。该参数允许资源栈集操作始终以指定的 max_concurrent_count 或 max_concurrent_percentage 操作资源栈实例。  * 此时不保证资源栈实例失败总数小于 failure_tolerance_count + 1，如果用户指定的是failure_tolerance_percentage的值，则不保证资源栈实例失败总数小于 failure_tolerance_percentage * 资源栈实例数 + 1。
        :type failure_tolerance_mode: str
        """
        
        

        self._region_concurrency_type = None
        self._region_order = None
        self._failure_tolerance_count = None
        self._failure_tolerance_percentage = None
        self._max_concurrent_count = None
        self._max_concurrent_percentage = None
        self._failure_tolerance_mode = None
        self.discriminator = None

        if region_concurrency_type is not None:
            self.region_concurrency_type = region_concurrency_type
        if region_order is not None:
            self.region_order = region_order
        if failure_tolerance_count is not None:
            self.failure_tolerance_count = failure_tolerance_count
        if failure_tolerance_percentage is not None:
            self.failure_tolerance_percentage = failure_tolerance_percentage
        if max_concurrent_count is not None:
            self.max_concurrent_count = max_concurrent_count
        if max_concurrent_percentage is not None:
            self.max_concurrent_percentage = max_concurrent_percentage
        if failure_tolerance_mode is not None:
            self.failure_tolerance_mode = failure_tolerance_mode

    @property
    def region_concurrency_type(self):
        """Gets the region_concurrency_type of this OperationPreferences.

        部署资源栈实例时区域（region）的执行策略，分为两种，SEQUENTIAL和PARALLEL，区分大小写，默认值为SEQUENTIAL  详细介绍：  * `SEQUENTIAL`：顺序执行，执行完一个region下的全部资源栈实例后再去执行另一个region。默认顺序执行。  * `PARALLEL`：并发执行，并发部署所有指定区域的资源栈实例。

        :return: The region_concurrency_type of this OperationPreferences.
        :rtype: str
        """
        return self._region_concurrency_type

    @region_concurrency_type.setter
    def region_concurrency_type(self, region_concurrency_type):
        """Sets the region_concurrency_type of this OperationPreferences.

        部署资源栈实例时区域（region）的执行策略，分为两种，SEQUENTIAL和PARALLEL，区分大小写，默认值为SEQUENTIAL  详细介绍：  * `SEQUENTIAL`：顺序执行，执行完一个region下的全部资源栈实例后再去执行另一个region。默认顺序执行。  * `PARALLEL`：并发执行，并发部署所有指定区域的资源栈实例。

        :param region_concurrency_type: The region_concurrency_type of this OperationPreferences.
        :type region_concurrency_type: str
        """
        self._region_concurrency_type = region_concurrency_type

    @property
    def region_order(self):
        """Gets the region_order of this OperationPreferences.

        区域（region）部署顺序。只有当用户指定region_concurrency_type为SEQUENTIAL时才会允许指定该参数。用户指定部署region的顺序，不允许出现资源栈集管理之外的region。  如果不指定，实际部署region顺序随机。部署顺序仅在当次部署时生效，应该包含且仅包含本次部署的所有region。

        :return: The region_order of this OperationPreferences.
        :rtype: list[str]
        """
        return self._region_order

    @region_order.setter
    def region_order(self, region_order):
        """Sets the region_order of this OperationPreferences.

        区域（region）部署顺序。只有当用户指定region_concurrency_type为SEQUENTIAL时才会允许指定该参数。用户指定部署region的顺序，不允许出现资源栈集管理之外的region。  如果不指定，实际部署region顺序随机。部署顺序仅在当次部署时生效，应该包含且仅包含本次部署的所有region。

        :param region_order: The region_order of this OperationPreferences.
        :type region_order: list[str]
        """
        self._region_order = region_order

    @property
    def failure_tolerance_count(self):
        """Gets the failure_tolerance_count of this OperationPreferences.

        容错次数。用户定义在每个区域（region）下，允许部署失败的资源栈实例数量。该参数取值默认为0，限定0和正整数。  如果定义region顺序执行（region_concurrency_type值为SEQUENTIAL），在某个region超过容错次数时，资源栈集会取消所有状态仍处于WAIT_IN_PROGRESS状态的实例。被取消的实例状态最终变为CANCEL_COMPLETE；  如果是region并行执行（region_concurrency_type值为PARALLEL），在某个region超过容错次数时，资源栈集只会取消该region下所有处于WAIT_IN_PROGRESS状态的实例。被取消的实例状态最终变为CANCEL_COMPLETE。  对处于OPERATION_IN_PROGRESS，或已经部署完成，即处于OPERATION_COMPLETE或者OPERATION_FAILED状态的资源栈实例，不受影响，状态不变。  failure_tolerance_count  和 failure_tolerance_percentage 仅能有一个存在。

        :return: The failure_tolerance_count of this OperationPreferences.
        :rtype: int
        """
        return self._failure_tolerance_count

    @failure_tolerance_count.setter
    def failure_tolerance_count(self, failure_tolerance_count):
        """Sets the failure_tolerance_count of this OperationPreferences.

        容错次数。用户定义在每个区域（region）下，允许部署失败的资源栈实例数量。该参数取值默认为0，限定0和正整数。  如果定义region顺序执行（region_concurrency_type值为SEQUENTIAL），在某个region超过容错次数时，资源栈集会取消所有状态仍处于WAIT_IN_PROGRESS状态的实例。被取消的实例状态最终变为CANCEL_COMPLETE；  如果是region并行执行（region_concurrency_type值为PARALLEL），在某个region超过容错次数时，资源栈集只会取消该region下所有处于WAIT_IN_PROGRESS状态的实例。被取消的实例状态最终变为CANCEL_COMPLETE。  对处于OPERATION_IN_PROGRESS，或已经部署完成，即处于OPERATION_COMPLETE或者OPERATION_FAILED状态的资源栈实例，不受影响，状态不变。  failure_tolerance_count  和 failure_tolerance_percentage 仅能有一个存在。

        :param failure_tolerance_count: The failure_tolerance_count of this OperationPreferences.
        :type failure_tolerance_count: int
        """
        self._failure_tolerance_count = failure_tolerance_count

    @property
    def failure_tolerance_percentage(self):
        """Gets the failure_tolerance_percentage of this OperationPreferences.

        容错百分比。定义每个区域（region）下，允许部署失败的资源栈实例数占该region下所有资源栈实例数的百分比。该参数取值默认为0，限定0和正整数。  通过容错百分比*资源栈实例数，并向下取整，得到实际容错次数。  failure_tolerance_count  和 failure_tolerance_percentage 仅能有一个存在。

        :return: The failure_tolerance_percentage of this OperationPreferences.
        :rtype: int
        """
        return self._failure_tolerance_percentage

    @failure_tolerance_percentage.setter
    def failure_tolerance_percentage(self, failure_tolerance_percentage):
        """Sets the failure_tolerance_percentage of this OperationPreferences.

        容错百分比。定义每个区域（region）下，允许部署失败的资源栈实例数占该region下所有资源栈实例数的百分比。该参数取值默认为0，限定0和正整数。  通过容错百分比*资源栈实例数，并向下取整，得到实际容错次数。  failure_tolerance_count  和 failure_tolerance_percentage 仅能有一个存在。

        :param failure_tolerance_percentage: The failure_tolerance_percentage of this OperationPreferences.
        :type failure_tolerance_percentage: int
        """
        self._failure_tolerance_percentage = failure_tolerance_percentage

    @property
    def max_concurrent_count(self):
        """Gets the max_concurrent_count of this OperationPreferences.

        每个区域（region）下可同时部署资源栈实例的最大账户数。该参数取值默认为1，限定为正整数。  最大并发账户数最多比容错次数多1。如果用户指定failure_tolerance_percentage，最大并发账户数最多比 failure_tolerance_percentage * 资源栈实例数多1。保证部署在所需的容错级别停止。  max_concurrent_count 和 max_concurrent_percentage 仅能有一个存在。

        :return: The max_concurrent_count of this OperationPreferences.
        :rtype: int
        """
        return self._max_concurrent_count

    @max_concurrent_count.setter
    def max_concurrent_count(self, max_concurrent_count):
        """Sets the max_concurrent_count of this OperationPreferences.

        每个区域（region）下可同时部署资源栈实例的最大账户数。该参数取值默认为1，限定为正整数。  最大并发账户数最多比容错次数多1。如果用户指定failure_tolerance_percentage，最大并发账户数最多比 failure_tolerance_percentage * 资源栈实例数多1。保证部署在所需的容错级别停止。  max_concurrent_count 和 max_concurrent_percentage 仅能有一个存在。

        :param max_concurrent_count: The max_concurrent_count of this OperationPreferences.
        :type max_concurrent_count: int
        """
        self._max_concurrent_count = max_concurrent_count

    @property
    def max_concurrent_percentage(self):
        """Gets the max_concurrent_percentage of this OperationPreferences.

        最大并发账户百分比，每个区域（region）中可同时部署的资源栈实例的最大账户百分比。该参数取值默认为1，限定正整数。  RFS根据百分比 *（每个region下资源栈实例数）得到的值，再向下取整，得到实际最大并发账户数。如果实际最大并发账户数向下取整值为0时，则默认选择最大并发账户数为1。  通过百分比计算得到的实际最大并发账户数最多比容错次数多1。如果用户指定failure_tolerance_percentage，实际最大并发账户数最多比 failure_tolerance_percentage * 资源栈实例数多1。保证部署在所需的容错级别停止。  max_concurrent_count 和 max_concurrent_percentage 仅能有一个存在。

        :return: The max_concurrent_percentage of this OperationPreferences.
        :rtype: int
        """
        return self._max_concurrent_percentage

    @max_concurrent_percentage.setter
    def max_concurrent_percentage(self, max_concurrent_percentage):
        """Sets the max_concurrent_percentage of this OperationPreferences.

        最大并发账户百分比，每个区域（region）中可同时部署的资源栈实例的最大账户百分比。该参数取值默认为1，限定正整数。  RFS根据百分比 *（每个region下资源栈实例数）得到的值，再向下取整，得到实际最大并发账户数。如果实际最大并发账户数向下取整值为0时，则默认选择最大并发账户数为1。  通过百分比计算得到的实际最大并发账户数最多比容错次数多1。如果用户指定failure_tolerance_percentage，实际最大并发账户数最多比 failure_tolerance_percentage * 资源栈实例数多1。保证部署在所需的容错级别停止。  max_concurrent_count 和 max_concurrent_percentage 仅能有一个存在。

        :param max_concurrent_percentage: The max_concurrent_percentage of this OperationPreferences.
        :type max_concurrent_percentage: int
        """
        self._max_concurrent_percentage = max_concurrent_percentage

    @property
    def failure_tolerance_mode(self):
        """Gets the failure_tolerance_mode of this OperationPreferences.

        资源栈集操作部署的失败容忍模式，分为两种，STRICT_FAILURE_TOLERANCE和SOFT_FAILURE_TOLERANCE，区分大小写，默认值为STRICT_FAILURE_TOLERANCE。  详细介绍：  * `STRICT_FAILURE_TOLERANCE`：此选项会动态降低并发级别，以确保同region下部署失败的账户数量永远不超过 failure_tolerance_count + 1。当用户指定failure_tolerance_percentage时，确保同region下部署失败的账户数量不超过 failure_tolerance_percentage * 资源栈实例数 + 1。  * 初始实际最大并发数为max_concurrent_count，如果用户指定的是max_concurrent_percentage，则初始实际最大并发数为 max_concurrent_percentage * 资源栈实例数，随后，实际最大并发数会根据失败次数增加而减少。  * `SOFT_FAILURE_TOLERANCE`：此选项将failure_tolerance_count (failure_tolerance_percentage) 与实际并发数分离开。该参数允许资源栈集操作始终以指定的 max_concurrent_count 或 max_concurrent_percentage 操作资源栈实例。  * 此时不保证资源栈实例失败总数小于 failure_tolerance_count + 1，如果用户指定的是failure_tolerance_percentage的值，则不保证资源栈实例失败总数小于 failure_tolerance_percentage * 资源栈实例数 + 1。

        :return: The failure_tolerance_mode of this OperationPreferences.
        :rtype: str
        """
        return self._failure_tolerance_mode

    @failure_tolerance_mode.setter
    def failure_tolerance_mode(self, failure_tolerance_mode):
        """Sets the failure_tolerance_mode of this OperationPreferences.

        资源栈集操作部署的失败容忍模式，分为两种，STRICT_FAILURE_TOLERANCE和SOFT_FAILURE_TOLERANCE，区分大小写，默认值为STRICT_FAILURE_TOLERANCE。  详细介绍：  * `STRICT_FAILURE_TOLERANCE`：此选项会动态降低并发级别，以确保同region下部署失败的账户数量永远不超过 failure_tolerance_count + 1。当用户指定failure_tolerance_percentage时，确保同region下部署失败的账户数量不超过 failure_tolerance_percentage * 资源栈实例数 + 1。  * 初始实际最大并发数为max_concurrent_count，如果用户指定的是max_concurrent_percentage，则初始实际最大并发数为 max_concurrent_percentage * 资源栈实例数，随后，实际最大并发数会根据失败次数增加而减少。  * `SOFT_FAILURE_TOLERANCE`：此选项将failure_tolerance_count (failure_tolerance_percentage) 与实际并发数分离开。该参数允许资源栈集操作始终以指定的 max_concurrent_count 或 max_concurrent_percentage 操作资源栈实例。  * 此时不保证资源栈实例失败总数小于 failure_tolerance_count + 1，如果用户指定的是failure_tolerance_percentage的值，则不保证资源栈实例失败总数小于 failure_tolerance_percentage * 资源栈实例数 + 1。

        :param failure_tolerance_mode: The failure_tolerance_mode of this OperationPreferences.
        :type failure_tolerance_mode: str
        """
        self._failure_tolerance_mode = failure_tolerance_mode

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
        if not isinstance(other, OperationPreferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
